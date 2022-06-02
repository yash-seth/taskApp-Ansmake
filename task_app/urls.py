from django.urls import re_path 
from task_app import views 
 
urlpatterns = [ 
    re_path(r'^task/new$', views.createTask),
    re_path(r'^task/all$', views.fetchTasks),
]