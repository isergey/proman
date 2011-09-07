from django.conf.urls.defaults import *


urlpatterns = patterns('tasks.views',
    url(r'^$', 'index' , name="tasks_index"),
    url(r'^project/(?P<id>\d+)/$', 'project_detail' , name="tasks_project_detail"),
    url(r'^milestone/(?P<id>\d+)/$', 'milestone_detail' , name="tasks_milestone_detail"),
    url(r'^milestone/(?P<id>\d+)/task/create/$', 'task_create' , name="tasks_task_create"),
    url(r'^task/(?P<id>\d+)/$', 'task_detail' , name="tasks_task_detail"),

)