# _*_coding:utf-8_*_
# Author:xupan
from carry.views.basesite import BasefuncModal
from carry.service import carry


class MenuAdmin(carry.BaseCarryModal):
    list_display = ['caption', 'parent', BasefuncModal.edit_field]

    actions = []
