# _*_coding:utf-8_*_
from carry.views.basesite import BasefuncModal
from carry.service import carry


class UserAdmin(carry.BaseCarryModal):
    list_display = ['username', 'email', BasefuncModal.edit_field]

    actions = []
