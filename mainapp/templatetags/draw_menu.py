from django import template
from django.shortcuts import get_object_or_404
from ..models import Item


register = template.Library()


@register.inclusion_tag('menu.html', takes_context=True)
def draw_menu(context, name: str):
    print(name)
    menu = Item.objects.filter(title=name)
    if menu.exists():
        parent = menu.first()

        item = get_object_or_404(Item, pk=context.get('pk'))
        while item and item.parent != parent:
            item = item.parent

        children = Item.objects.filter(parent=parent)

        return {
            'success': True,
            'parent': parent,
            'item': item,
            'children': children,
            'pk': context.get('pk'),
        }

    return {
        'success': False
    }
