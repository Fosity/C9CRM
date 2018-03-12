# _*_coding:utf-8_*_
from carry.service import carry
from carry.views.basesite import BasefuncModal


class UserAdmin(carry.BaseCarryModal):
    list_display = ['username', 'email', BasefuncModal.edit_field]

    actions = []
