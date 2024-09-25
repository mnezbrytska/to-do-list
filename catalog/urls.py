from django.urls import path

from catalog.views import TaskListView, TagListView, TaskCreateView, TaskUpdateView, TaskDeleteView, TagCreateView, \
    TagUpdateView, TagDeleteView, task_change_complete

urlpatterns = [
    path('', TaskListView.as_view(), name='index'),
    path('tags/', TagListView.as_view(), name='tag-list'),
    path('task/add/', TaskCreateView.as_view(), name='task-create'),
    path('task/<int:pk>/update/', TaskUpdateView.as_view(), name='task-update'),
    path('task/<int:pk>/delete/', TaskDeleteView.as_view(), name='task-delete'),
    path('tags/add/', TagCreateView.as_view(), name='tag-create'),
    path('tags/<int:pk>/update/', TagUpdateView.as_view(), name='tag-update'),
    path('tags/<int:pk>/delete/', TagDeleteView.as_view(), name='tag-delete'),
    path('task/<int:pk>/toggle/', task_change_complete, name='task-change-complete'),

]


app_name = "catalog"