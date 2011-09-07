# encoding: utf-8
from  django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse

from models import Project, Milestone, Task
from forms import TaskForm

def index(request):
    projects = Project.objects.all()

    return render(request, 'projects.html', {
        'projects': projects,
        })


def project_detail(request, id):
    project = Project.objects.get(pk=id)
    milestones = Milestone.objects.filter(project=project)
    return render(request, 'project_detail.html', {
        'project': project,
        'milestones': milestones,
        })


def milestone_detail(request, id):
    milestone = Milestone.objects.get(pk=id)
    tasks = Task.objects.filter(milestone=milestone)
    return render(request, 'milestone_detail.html', {
        'milestone': milestone,
        'tasks': tasks,
        })


def task_detail(request, id):
    task = Task.objects.get(pk=id)
    return render(request, 'task_detail.html', {
        'task': task,
        })


def task_create(request, id):
    milestone = get_object_or_404(Milestone, pk=id)
    if request.method == 'POST': # If the form has been submitted...
        post = request.POST.copy()
        post['milestone']=milestone.id
        form = TaskForm(data=post) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            form.save()
            # Process the data in form.cleaned_data
            # ...
            return redirect('/tasks') # Redirect after POST
    else:
        form = TaskForm(
            milestone=milestone,
            initial={
                'milestone': milestone,
                },
        )
        # An unbound form
        #from django import forms
        #form.depends_from = forms.ModelMultipleChoiceField(queryset=Task.objects.filter(milestone=milestone))
    return render(request, 'task_create.html', {
        'milestone': milestone,
        'form': form,
        })


def task_edit(request, id):
    task = Task.objects.get(pk=id)
    return render(request, 'task_detail.html', {
        'task': task,
        })
