# encoding: utf-8
from  django.shortcuts import render
from models import Project, Milestone, Task

def index(request):
    projects = Project.objects.all()

    return render(request, 'projects.html',{
        'projects': projects,
    })

def project_detail(request, id):
    project = Project.objects.get(pk=id)
    milestones = Milestone.objects.filter(project=project)
    return render(request, 'project_detail.html',{
        'project': project,
        'milestones': milestones,
    })