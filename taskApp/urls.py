from django.urls import path

from . import views


urlpatterns = [
    path('', view=views.home, name='home'),
    path('tasks/', view=views.create_task, name='task')
]
