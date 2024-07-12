from django.urls import path
from . import views

urlpatterns = [
    path('project_config/', views.foo),
    path('project_config/<product>/', views.foo),
    path('project_config/<product>/<project_id>/', views.foo),
]
