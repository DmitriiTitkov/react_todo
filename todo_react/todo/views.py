from django.core.exceptions import ObjectDoesNotExist
from rest_framework.exceptions import NotFound
from rest_framework.viewsets import ModelViewSet

from todo.models import TaskList, Task
from todo.serializers import TaskListSerialazer, TaskSerialazer


class TaskListViewSet(ModelViewSet):
    queryset = TaskList.objects.all()
    serializer_class = TaskListSerialazer
    lookup_url_kwarg = "list_pk"


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerialazer
    lookup_url_kwarg = "task_pk"

    def get_queryset(self):
        qs = Task.objects.all()
        list_pk = self.kwargs.get("list_pk")
        if list_pk:
            try:
                TaskList.objects.get(pk=list_pk)
            except TaskList.DoesNotExist:
                raise NotFound(detail=f"List with id {list_pk} doesn't exist")
            qs = qs.filter(task_list=list_pk)

        return qs
