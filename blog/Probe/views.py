from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import ProbeModelDetail,ProbeList
# Create your views here.

class ProbeModelListView(ListView):
    model = ProbeModelDetail
    template_name = 'Probe_model_list.html'

class ProbeListVView(ListView):
    model = ProbeList
    template_name = 'Probe_list_by_model.html'