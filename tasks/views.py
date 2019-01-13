from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required

from .models import  Task
from .forms import TaskForm



@login_required
def task_list(request):
    tasks = Task.objects.all().order_by("-created_at")

    task_form = TaskForm()

    context = {
        'tasks': tasks,
        'task_form': task_form
    }
    return render(request, "tasks/tasks.html", context)


@login_required
@require_POST
def add_task(request):
    # task_form = TaskForm()
    if request.method == 'POST':
        task_form = TaskForm(request.POST)

        if task_form.is_valid():
            task_form.save()

    return redirect("task_list")


@login_required
def task_completed(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.done = True
    task.save()
    return redirect("task_list")


# @login_required
# def remove_task(request, pk):
#     task = get_object_or_404(Task, pk=pk)
#     task.delete()
#     return redirect("task_list")


@login_required
def remove_completed(request):
    Task.objects.filter(done__exact=True).delete()
    return redirect("task_list")


@login_required
def remove_all_tasks(request):
    Task.objects.all().delete()
    return redirect("task_list")