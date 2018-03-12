# Create your models here.
from django.db import models

from carry import models as carry_models


class Task(models.Model):
    nid = models.BigAutoField(verbose_name='任务编号', primary_key=True)
    title = models.CharField(verbose_name='任务名称', max_length=128)
    from_user = models.ForeignKey(carry_models.User, verbose_name='任务来源', related_name='from_user')
    to_user = models.ForeignKey(carry_models.User, verbose_name='任务接收', related_name='to_user')
    status_choices = [
        (1, '已经完成'), (2, '还未完成'), (3, '有困难'), (4, '超期'), (5, '延期')
    ]
    status = models.IntegerField(verbose_name='任务状态', choices=status_choices, default=2)
    reply = models.ForeignKey(verbose_name='关联上级任务', to='self', null=True, blank=True)
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    wish_finish_time = models.DateTimeField(verbose_name='预计完成时间', null=True, blank=True)
    finish_time = models.DateTimeField(verbose_name='实际完成时间', null=True, blank=True)
    finish_Fk = models.ForeignKey(verbose_name='选择完成的类型', to='TaskType', null=True, blank=True)
    finish_cost_time = models.CharField(verbose_name='任务花费时间，请填写小时', max_length=128, null=True, blank=True)

    finish_content = models.TextField(verbose_name='完成内容：请填写完成的方式，以及生成物', blank=True, null=True)
    introduction_content = models.TextField(verbose_name='任务来源，介绍，以及完成方法')

    def __str__(self):
        return self.title


class TaskType(models.Model):
    nid = models.BigAutoField(verbose_name='任务类型编号', primary_key=True)
    title = models.CharField(verbose_name='类型名称', max_length=128)
    score = models.CharField(verbose_name='获得分数', max_length=128)
    diff_level = models.CharField(verbose_name='难易程度', max_length=128)

    def __str__(self):
        return self.title
