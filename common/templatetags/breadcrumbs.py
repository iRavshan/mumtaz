from django import template

register = template.Library()

@register.inclusion_tag('shared/_breadcrumbs.html', takes_context=True)
def render_breadcrumbs(context, *crumbs):
    return {'breadcrumbs': crumbs}