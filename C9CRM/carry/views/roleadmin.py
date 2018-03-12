# _*_coding:utf-8_*_
# Author:xupan
from carry.service import carry
from carry.views.basesite import BasefuncModal


class RoleAdmin(carry.BaseCarryModal):
    list_display = ['caption', BasefuncModal.edit_field]

    actions = []
