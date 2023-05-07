from django import template


register = template.Library()


@register.inclusion_tag('children.html', takes_context=False)
def draw_children(parent: dict):
    return {"parent": parent}
