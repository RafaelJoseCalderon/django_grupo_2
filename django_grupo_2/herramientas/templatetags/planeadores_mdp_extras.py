from django import template
from django.utils.safestring import mark_safe
from django.utils.html import format_html
from itertools import chain

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

@register.simple_tag
def render_js_defer(form):
    returned_value = ""

    for path in form.media._js:
        if hasattr(path, "__html__"):
            returned_value += path.__html__()
        else:
            returned_value += format_html(
                '<script defer src="{}"></script>',
                form.media.absolute_path(path)
            )

    return mark_safe(returned_value)

@register.simple_tag
def render_css_defer(form):
    returned_value = ""

    media = sorted(form.media._css)
    for medium in media:
        for path in form.media._css[medium]:
            if hasattr(path, "__html__"):
                returned_value += path.__html__()
            else:
                returned_value += format_html(
                    '<link href="{}" media="{}" rel="stylesheet">',
                    form.media.absolute_path(path),
                    medium,
                )

    return mark_safe(returned_value)

@register.filter(name='has_group')
def has_group(request, group):
    return request.user.groups.filter(name=group).exists()
