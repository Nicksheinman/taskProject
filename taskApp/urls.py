from django.urls import path
from django.views.i18n import JavaScriptCatalog

from . import views


urlpatterns = [
    path('', view=views.home, name='home'),
    path('tasks/', view=views.create_task, name='task'),
    path('update/<int:pk>/', view=views.update, name='update'),
    path('create/', view=views.create, name='create'),
    path('dashboard/delete/<int:pk>', view=views.deleteT, name='delete'),
    path('register/', view=views.register, name='register'),
    path('login/', view=views.login, name='login'),
    path('dashboard/', view=views.dashboard, name='dashboard'),
    path('logout/', view=views.logout, name='logout')
]
