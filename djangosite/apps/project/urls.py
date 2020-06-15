from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('create_project', views.create_project, name='create_project'),
    path('list', views.tasks_list, name='tasks_list'),
    path('upload_files/<str:name>/', views.upload_files, name='detail'),
]