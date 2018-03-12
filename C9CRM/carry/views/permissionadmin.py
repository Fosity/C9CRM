# _*_coding:utf-8_*_
# Author:xupan
from django.conf import settings
from django.shortcuts import render

from carry.service import carry
from carry.views.basesite import BasefuncModal


class PermissionAdmin(carry.BaseCarryModal):
    list_display = ['caption', 'url', 'menu', BasefuncModal.edit_field]

    actions = []

    def another_urls(self):
        from django.conf.urls import url
        info = self.model_class._meta.app_label, self.model_class._meta.model_name
        urls = [
            url(r'^show/$', self.show, name='%s_%s_show' % info),
        ]
        return urls

    def show(self, request):
        permission_url_list = request.session.get(settings.RBAC_PERMISSION_URL_SESSION_KEY)
        tpl = "你的权限有：<br/>" + ("<br/>".join(permission_url_list))
        return render(request, 'permission_show.html', {'tpl': tpl})
