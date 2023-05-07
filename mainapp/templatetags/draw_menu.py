from django import template
from ..models import Item


register = template.Library()


def serialize(item):
    result = {
        'id': item.id,
        'title': item.title,
        'parent_id': item.parent_id,
        'is_root': True if item.parent_id is None else False,
        'children': [],
        'is_open': False,
        'is_active': False,
    }
    return result


def build_tree(items_dict, parent):
    for _, item in items_dict.items():
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
        if items_dict[item.id]['is_root']:
            root = items_dict[item.id]

    if root is None:
        return {
            'success': False,
            'detail': f"{title} is empty or does not exist."
            }

    active_id = context.get('pk')
    if active_id in items_dict:
        active_item = items_dict[active_id]
        active_item['is_active'] = True
        while active_item['parent_id']:
            active_item = items_dict[active_item['parent_id']]
            active_item['is_active'] = True

    build_tree(items_dict, root)
    return {
        'success': True,
        'root': root,
    }
