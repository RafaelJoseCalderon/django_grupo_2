from abc import ABC
from urllib import parse

from django.views.generic.list import ListView
from django.db.models import Q


class ListViewWithSearch(ListView, ABC):
    page_title = None
    class_form = None
    search_dict = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = self.page_title
        context['form'] = self.class_form(self.request.GET)

        return context

    def get_queryset(self):
        query = super().get_queryset()

        request_get = self.request.GET
        search_params = self.search_params(request_get)
        query_params = self.query_params(search_params)

        return query.filter(query_params)

    def query_params(self, params):
        return Q(**{k: v for k, v in params.items() if v not in (None, '')})

    def search_params(self, params):
        dict_ = self.search_dict
        return {dict_.get(k, k): v for k, v in params.items() if k in dict_}


class ListViewWithSearchAndPagination(ListViewWithSearch, ABC):
    url_page = None
    page_kwarg = 'pagina'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.paginate_by is not None:
            context['url_params'] = self.url_params()
            context['page_list'] = self.set_paginator(context['page_obj'])

        return context

    def url_params(self):
        url_params = parse.urlencode(
            {k: v for k, v in self.request.GET.items() if k != 'pagina'}
        )

        return f'?{url_params}&pagina' if url_params else f'?pagina'

    def set_paginator(self, page_obj):
        return page_obj.paginator.get_elided_page_range(
            page_obj.number,
            on_each_side = 0,
            on_ends = 1
        )