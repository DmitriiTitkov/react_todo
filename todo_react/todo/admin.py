from django.contrib import admin
from .models import TaskList, Task

@admin.register(TaskList)
class TaskListAdmin(admin.ModelAdmin):
    pass

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    pass