from rest_framework.relations import PrimaryKeyRelatedField
from rest_framework.serializers import ModelSerializer

from todo.models import TaskList, Task


class TaskListSerialazer(ModelSerializer):
    lookup_url_kwarg = "list_pk"

    class Meta:
        model = TaskList
        fields = "__all__"


class TaskSerialazer(ModelSerializer):
    lookup_url_kwarg = "task_pk"

    class Meta:
        model = Task
        fields = "__all__"
