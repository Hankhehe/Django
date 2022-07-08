from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProbeDashboard),
    path('Models', views.ProbeModelListView.as_view()),
    path('Probes', views.ProbeListVView.as_view()),
]