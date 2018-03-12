# -*- coding: utf-8 -*-

from task.views.service import taskconfig


def menu_time_create():
    '''产生任务报告的menu'''
    menu = []
    for k, v in taskconfig.task_config.items():
        menu_dict = {}
        menu_dict['menu'] = v.get('menu')
        menu_dict['nid'] = k
        menu.append(menu_dict)
    return menu


class Taskget(object):
    '''根据，配置文件，自定义搜索条件'''
    def __init__(self, month, cls_obj):
        self.task_config = taskconfig.task_config
        self.month = month
        self.config_month = self.task_config.get(self.month)
        self.cls_obj = cls_obj
        self.status = self.config_month.get('status')
        self.select_args = self.config_month.get('select_args')
        self.title = self.config_month.get('title')
        self.data_obj = {}

    def models_data_filter(self):
        if self.status:
            for k, v in self.status.items():
                self.data_obj[k] = self.cls_obj.filter(status__in=v)
        else:
            pass

    def data_time_filter(self):
        time_name1 = self.select_args.get('time_name')
        time_name = time_name1 + '__range'
        time_ = self.select_args.get('time').split('/')
        for k, v in self.data_obj.items():
            data_dict = {
                time_name: [time_[0], time_[1]]
            }
            self.data_obj[k] = v.filter(**data_dict).extra(
                select={time_name1: "strftime('%%s',strftime('%%Y-%%m-%%d',finish_time))"})

    def models_data_values(self):
        if self.select_args:
            group_by_name = self.select_args.get('group_by')
            for k, v in self.data_obj.items():
                self.data_obj[k] = v.values(*group_by_name)
    def models_data_annotate(self):
        from django.db.models import Count
        id_name = self.select_args.get('id_name')
        if self.config_month.get('y_axis', {}).get('type') == 'num':
            for k, v in self.data_obj.items():
                self.data_obj[k] = list(v.annotate(ct=Count(id_name)))
    def run(self):
        self.models_data_filter()
        self.data_time_filter()
        self.models_data_values()
        self.models_data_annotate()


class TaskProcess(Taskget):
    def change_data_process(self):
        self.run()
        data = None
        if self.config_month.get('type') == 'pie':
            data = self.data_change_pie()
        elif self.config_month.get('type') == 'line':
            data = self.data_change_line()
        else:
            pass
        response = {
            'series': data,
            'type': self.config_month.get('type'),
            'title': self.config_month.get('title')
        }
        return response

    def data_change_pie(self):
        """pie 图 数据格式[['name',num],['name',num]]"""
        pie_dict = {}
        for k, v in self.data_obj.items():
            pie_dict[k] = {}
            pie_dict[k]['name'] = self.title.get(k)
            pie_dict[k]['data'] = []
            for item in self.data_obj.get(k):
                pie_dict[k]['data'].append([item.get(self.select_args.get('group_by')[0]), item.get('ct')])
        return pie_dict

    def data_change_line(self):
        """折线图 数据格式[['time','num'],[]]"""
        line_dict = {}
        for k, v in self.data_obj.items():
            line_dict[k] = {}
            line_dict[k]['name'] = self.title.get(k)
            line_dict[k]['data'] = []
            for item in self.data_obj.get(k):
                line_dict[k]['data'].append([item.get(self.select_args.get('group_by')[1]), item.get('ct')])
        return line_dict
