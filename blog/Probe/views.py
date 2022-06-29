from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import ProbeModelDetail,ProbeList
# Create your views here.

class ProbeModelListView(ListView):
    model = ProbeModelDetail
    template_name = 'Probe_model_list.html'

class ProbeModelDetailView(DetailView):
    model = ProbeModelDetail
    template_name = 'Probe_model_detail.html'