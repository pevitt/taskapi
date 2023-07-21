from django.urls import path
from tasks.views import TaskView, TaskStatusView, TaskViewIndicator

urlpatterns = [
    path(
        '',
        TaskView.as_view(),
        name='task-view'
    ),
    path(
        'status/',
        TaskStatusView.as_view(),
        name='task-status-view'
    ),
    path(
        'indicator/<uuid:person_id>/',
        TaskViewIndicator.as_view(),
        name='task-indicator-view'
    )
]