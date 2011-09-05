from django.conf.urls.defaults import *


urlpatterns = patterns('tasks.views',
    url(r'^$', 'index' , name="tasks_index"),
    url(r'^project/(?P<id>\d+)/$', 'project_detail' , name="tasks_project_detail"),
)