from django import template
from ..models import Item


register = template.Library()


def serialize(item):
    result = {
        'id': item.id,
        'title': item.title,
        'parent_id': item.parent_id,
        'is_root': True if item.parent_id is not None else False,
        'children': [],
        'is_open': False,
        'is_active': False,
        'active_child': None,
    }
    return result


def build_tree(items_dict, parent):
    for item in items_dict:
        if item['parent_id'] == parent['id']:
            parent['children'].append(item)
            if item['is_active']:
                build_tree(items_dict, item)


@register.inclusion_tag('menu.html', takes_context=True)
def draw_menu(context, title: str):
    items_dict = {}
    root = None
    for item in Item.objects.filter(menu_title__title=title):
        items_dict[item.id] = serialize(item)
        if item['is_root']:
            root = item

    active_id = context.get('pk')
    active_item = items_dict[active_id]
    while active_item:
        active_item['is_active'] = True
        active_item = items_dict[active_item['parent_id']]

    build_tree(items_dict, root)
    return {"tree": root}


# @register.inclusion_tag('menu.html', takes_context=True)
# def draw_menu(context, title: str):
#     menu = Item.objects.filter(title=title)
#     if menu.exists():
#         parent = menu.first()
#
#         item = get_object_or_404(Item, pk=context.get('pk'))
#         while item and item.parent != parent:
#             item = item.parent
#
#         children = Item.objects.filter(parent=parent)
#
#         return {
#             'success': True,
#             'parent': parent,
#             'item': item,
#             'children': children,
#             'pk': context.get('pk'),
#         }
#
#     return {
#         'success': False
#     }
