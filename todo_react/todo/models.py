from django.db import models


class TaskList(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()


class Task(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    due_date = models.DateTimeField()
    task_list = models.ForeignKey(to=TaskList, on_delete=models.CASCADE, related_name="tasks")
