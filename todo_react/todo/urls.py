from django.urls.conf import path
from rest_framework import routers

from todo.views import TaskListViewSet, TaskViewSet

router = routers.DefaultRouter()
router.register(r'task-lists', TaskListViewSet)
router.register(r'tasks', TaskViewSet)

task_list = TaskViewSet.as_view(actions={
        'get': 'list',
        'post': 'create'
})

task_detail = TaskViewSet.as_view(actions={
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = [
    path("task-lists/<int:list_pk>/tasks/", task_list),
    path("task-lists/<int:list_pk>/tasks/<int:task_pk>", task_detail)
]

urlpatterns += router.urls
