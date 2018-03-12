# Register your models here.
from carry.service import carry
from task import models
from task.views.taskadmin import TaskAdmin
from task.views.tasktypeadmin import TaskTypeAdmin

carry.site.register(models.Task, TaskAdmin)
carry.site.register(models.TaskType, TaskTypeAdmin)
