from django.urls import path
from . import views


urlpatterns = [
    path('', views.projects, name='projects'),
    path('projects/<str:pk>/', views.single_project, name='project'),
]
