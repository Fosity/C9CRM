# -*- coding: utf-8 -*-
import json
import os

from django.conf import settings
from django.http.request import QueryDict
from django.shortcuts import HttpResponse, redirect, render
from django.urls import reverse
from django.utils.safestring import mark_safe

from carry.service import carry
from task import models
from task.views import forms


class TaskAdmin(carry.BaseCarryModal):

    def list_item_filter(self, request):
        '''定义起始查询的条件
        查询 from_user 或者 to_user 字段中有关 登录用户 的查询结果
        '''
        # [{'a':a,'b':b},{'c':c}] ===> (a and b) or (c)
        return [{'from_user': request.session.get('user_info').get('nid')},
                {'to_user': request.session.get('user_info').get('nid')}]

    def edit_field(self, obj=None, is_header=False):
        '''操作栏，生成'''
        if is_header:
            return '操作'
        else:
            # url 尾部的 字段
            param_url = ""
            if len(self.request.GET):
                _change = QueryDict(mutable=True)
                _change['_change_filter'] = self.request.GET.urlencode()
                param_url = "?{0}".format(_change.urlencode())

            to_user_id = obj.to_user_id
            from_user_id = obj.from_user_id
            user_info_nid = self.request.session.get('user_info').get('nid')

            tpl_edit_url = "<a style='color:red'>编辑</a>"
            if str(obj.status) != '1' and user_info_nid is to_user_id:
                # 判断 任务状态是否完成，并且 任务处理人是否是登录用户
                edit_url = reverse('{0}:{1}_{2}_change'.format(self.site.namespace, self.app_label, self.model_name),
                                   args=(obj.pk,))
                tpl_edit_url = "<a href='{0}{1}'>编辑</a>".format(edit_url, param_url)

            tpl_del_url = "<a style='color:red'>删除</a>"
            if user_info_nid is from_user_id:
                # 判断 任务分发者 是当前登录用户，才有删除的功能
                del_url = reverse('{0}:{1}_{2}_delete'.format(self.site.namespace, self.app_label, self.model_name),
                                  args=(obj.pk,))
                tpl_del_url = "<a href='{0}{1}'>删除</a>".format(del_url, param_url)

            # 每个人都有查看详细页面的功能
            detail_url = reverse('{0}:{1}_{2}_detail'.format(self.site.namespace, self.app_label, self.model_name),
                                 args=(obj.pk,))
            tpl_detail_url = "<a href='{0}{1}'>查看详细</a>".format(detail_url, param_url)

            tpl_submit_url = '<a style="color:red">进入提交</a>'
            if user_info_nid is to_user_id:
                # 判断 当前登录用户是 任务处理者时，才能有编辑能力。
                submit_url = reverse('{0}:{1}_{2}_submit'.format(self.site.namespace, self.app_label, self.model_name),
                                     args=(obj.pk,))
                tpl_submit_url = "<a href='{0}{1}'>进入提交</a>".format(submit_url, param_url)

            tpl = "{0} | {1} | {2} | {3}".format(tpl_edit_url,
                                                 tpl_del_url,
                                                 tpl_detail_url,
                                                 tpl_submit_url)
            return mark_safe(tpl)

    def create_time(self, obj=None, is_header=False):
        """时间样式，颜色增加"""
        if is_header:
            return '创建时间'
        else:
            finish_time = obj.finish_time.strftime('%Y-%m-%d %H:%M')
            wish_finish_time = obj.wish_finish_time.strftime('%Y-%m-%d %H:%M')
            create_time = obj.create_time.strftime('%Y-%m-%d %H:%M')
            if finish_time > wish_finish_time:
                return mark_safe("<a style='color:red'>%s</a>" % create_time)
            else:
                return mark_safe("<a style='color:blue'>%s</a>" % create_time)

    def finish_time(self, obj=None, is_header=False):
        if is_header:
            return '完成时间'
        else:
            finish_time = obj.finish_time.strftime('%Y-%m-%d %H:%M')
            wish_finish_time = obj.wish_finish_time.strftime('%Y-%m-%d %H:%M')
            if finish_time > wish_finish_time:
                return mark_safe("<a style='color:red'>%s</a>" % finish_time)
            else:
                return mark_safe("<a style='color:blue'>%s</a>" % finish_time)

    def wish_finish_time(self, obj=None, is_header=False):
        if is_header:
            return '建议完成时间'
        else:
            finish_time = obj.finish_time.strftime('%Y-%m-%d %H:%M')
            wish_finish_time = obj.wish_finish_time.strftime('%Y-%m-%d %H:%M')
            if finish_time > wish_finish_time:
                return mark_safe("<a style='color:red'>%s</a>" % wish_finish_time)
            else:
                return mark_safe("<a style='color:blue'>%s</a>" % wish_finish_time)

    def status(self, obj=None, is_header=False):
        ''' 任务状态'''
        if is_header:
            return '任务状态'
        else:
            for item in models.Task.status_choices:
                if item[0] == obj.status:
                    menu = {
                        '1': '<div class="label label-table label-success">%s</div>',
                        '2': '<div class="label label-table label-info">%s</div>',
                        '3': '<div class="label label-table label-warning">%s</div>',
                        '4': '<div class="label label-table label-danger">%s</div>',
                        '5': '<div class="label label-table label-purple">%s</div>',
                    }
                    return mark_safe(menu[str(item[0])] % (item[1]))

    actions = []

    list_display = ['nid', 'title', 'from_user', 'to_user', create_time, wish_finish_time, finish_time, status, 'reply',
                    edit_field]

    def another_urls(self):
        from django.conf.urls import url
        info = self.model_class._meta.app_label, self.model_class._meta.model_name
        urls = [
            url(r'^submit/(?P<nid>\d+)/$', self.submit, name='%s_%s_submit' % info),
            url(r'^upload_img.html$', self.upload_img, name='upload_img'),
            url(r'^all_task_report.html$', self.all_task_report, name='all_task_report'),
            url(r'^report_ajax.html$', self.report_ajax, name='report_ajax'),
            url(r'^report_json.html$', self.report_json, name='report_json'),
        ]
        return urls

    def submit(self, request, nid):
        '''上传任务'''
        import datetime
        task_obj = models.Task.objects.filter(nid=nid)
        if request.method == "GET":
            task_form_obj = forms.taskForm()
            return render(request, 'task_submit.html', {'task_obj': task_obj, 'task_form': task_form_obj, 'num': nid})
        else:
            task_form_obj = forms.taskForm(request.POST)
            if task_form_obj.is_valid():
                models.Task.objects.filter(nid=nid).update(finish_time=datetime.datetime.now(), status=1,
                                                           **task_form_obj.cleaned_data)
                url = reverse('carry:task_task_changelist')
                return redirect(url)
            else:
                return HttpResponse('输入有误，格式不对')

    def upload_img(self, request):
        '''上传图片'''
        file_obj = request.FILES.get('imgFile')
        file_path = os.path.abspath(os.path.join(settings.BASE_DIR, 'task/static/imgs', file_obj.name))
        with open(file_path, 'wb') as f:
            for chunk in file_obj.chunks():
                f.write(chunk)
        dic = {
            'error': 0,
            'url': '/' + file_path,
            'message': '上传图片成功'
        }
        return HttpResponse(json.dumps(dic))

    def all_task_report(self, request):
        '''任务报告页'''
        if request.method == "GET":
            return render(request, 'task_report.html')

    def report_ajax(self, request):
        """ ajax 发送 任务报告页面显示menu"""
        if request.method == "POST":
            from task.views.service import task_func
            data = {
                'all_task': task_func.menu_time_create(),
            }
            return HttpResponse(json.dumps(data))

    def report_json(self, request):
        ''' ajax 发送 生成图表的 json 数据'''
        from task.views.service import task_func
        if request.method == "POST":
            content = {
                'status': False,
                'data': None,
            }
            menu1 = request.POST.get('menu1')
            data_change_obj = task_func.TaskProcess(month=menu1, cls_obj=models.Task.objects)
            rep = data_change_obj.change_data_process()
            content['data'] = rep
            content['status'] = True
            return HttpResponse(json.dumps(content))
