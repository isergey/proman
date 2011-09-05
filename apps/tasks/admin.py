# encoding: utf-8
from django.contrib import admin
from models import Project, Milestone, Task

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date', 'status')

admin.site.register(Project, ProjectAdmin)

class MilestoneAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date','priority' ,'status')

admin.site.register(Milestone, MilestoneAdmin)

class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date','priority' ,'status')

admin.site.register(Task, TaskAdmin)