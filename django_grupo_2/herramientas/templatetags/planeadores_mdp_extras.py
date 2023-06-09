from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def is_link_activate(context, url):
    return context.request.resolver_match.url_name == url


@register.simple_tag(takes_context=True)
def link_activate(context, url):
    url_name = context.request.resolver_match.url_name

    if url_name == url:
        return 'active'
    else:
        return ''
