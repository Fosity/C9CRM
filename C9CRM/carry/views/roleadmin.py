# _*_coding:utf-8_*_
# Author:xupan
from carry.views.basesite import BasefuncModal
from carry.service import carry


class RoleAdmin(carry.BaseCarryModal):
    list_display = ['caption', BasefuncModal.edit_field]

    actions = []
