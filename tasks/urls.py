from django.contrib import admin
from django.urls import path

from . import views as task_views

# app_name = 'tasks'

urlpatterns = [
    path('', task_views.task_list, name="task_list"),
    path('task/<int:pk>/', task_views.task_completed, name="task_completed"),
    path('task/add/', task_views.add_task, name="add_task"),
    path('task/removecompleted/', task_views.remove_completed, name="remove_completed"),
    path('task/removeall/', task_views.remove_all_tasks, name="remove_all"),
]
