from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProbeModelListView.as_view()),
    path('<pk>', views.ProbeListVView.as_view()),
]