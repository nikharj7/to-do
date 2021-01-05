from django.shortcuts import render,redirect
from home.models import Task

# Create your views here.

def home(request):
    context = {'success': False}
    if request.method == "POST":
        title = request.POST['title']
        desc = request.POST['desc']
        ins = Task(taskTitle=title, taskDesc=desc)
        ins.save()
        context = {'success': True}

    return render(request, 'index.html', context)


def task(request):
    allTasks = Task.objects.all()
    context = {'tasks':allTasks}
    return render(request, 'task.html', context)


def delete(request, todo_id):
    deltasks = Task.objects.get(id=todo_id)
    deltasks.delete()
    return redirect(task)
