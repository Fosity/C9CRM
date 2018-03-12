# -*- coding: utf-8 -*-  
from django.forms import Form, fields, widgets

from utils.xss import xss_defend


class taskForm(Form):
    '''任务输入框'''
    finish_content = fields.CharField(widget=widgets.Textarea(attrs={'id': 'f1'}))

    def clean_content(self):
        content_old = self.cleaned_data['content']
        return xss_defend(content_old)
