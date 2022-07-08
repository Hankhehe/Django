from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('Models', views.ProbeModelListView.as_view()),
    path('Probes', views.ProbeListVView.as_view()),
]