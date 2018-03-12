# _*_coding:utf-8_*_
# Author:xupan
from django.http.request import QueryDict
from django.urls import reverse
from django.utils.safestring import mark_safe

from carry.service import carry


class BasefuncModal(carry.BaseCarryModal):

    def edit_field(self, obj=None, is_header=False):
        if is_header:
            return '操作'
        else:

            edit_url = reverse('{0}:{1}_{2}_change'.format(self.site.namespace, self.app_label, self.model_name),
                               args=(obj.pk,))
            del_url = reverse('{0}:{1}_{2}_delete'.format(self.site.namespace, self.app_label, self.model_name),
                              args=(obj.pk,))
            detail_url = reverse('{0}:{1}_{2}_detail'.format(self.site.namespace, self.app_label, self.model_name),
                                 args=(obj.pk,))

            param_url = ""
            if len(self.request.GET):
                _change = QueryDict(mutable=True)
                _change['_change_filter'] = self.request.GET.urlencode()
                param_url = "?{0}".format(_change.urlencode())

            tpl = "<a href='{0}{3}'>编辑</a> | <a href='{1}{3}'>删除</a> | <a href='{2}{3}'>查看详细</a>".format(edit_url,
                                                                                                         del_url,
                                                                                                         detail_url,
                                                                                                         param_url)
            return mark_safe(tpl)
