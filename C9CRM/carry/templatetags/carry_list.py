# _*_coding:utf-8_*_
# Author:xupan
from types import FunctionType

from django.template import Library

register = Library()


def result_header_list(change_list):
    """
    处理表格头部
    :param modal_cls:
    :param list_display:
    :return:
    """
    if change_list.list_display == "__all__":
        yield change_list.carry_modal.model_name
    else:
        for name in change_list.list_display:
            yield name(change_list.carry_modal, is_header=True) \
                if isinstance(name, FunctionType) else change_list.model_cls._meta.get_field(
                name).verbose_name


def result_body_list(change_list):
    """
    处理表格内容
    :param queryset:
    :param list_display:
    :return:
    """
    for row in change_list.result_list:
        if change_list.list_display == "__all__":
            yield [str(row), ]
        else:
            yield [name(change_list.carry_modal, obj=row)
                   if isinstance(name, FunctionType) else getattr(row, name)
                   for name in change_list.list_display]


@register.inclusion_tag('carry/change_list_results.html')
def show_result_list(change_list):
    """
    展示数据表格
    1. 表头
    2. 表体
    """
    return {
        'result': result_body_list(change_list),
        'headers': result_header_list(change_list)
    }


@register.inclusion_tag('carry/change_list_action.html')
def show_action(change_list):
    return {'actions': ((item.__name__, item.short_description) for item in change_list.actions)}
