from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from .models import ProbeModelDetail,ProbeList
# Create your views here.

class ProbeModelListView(generic.ListView):
    model = ProbeModelDetail
    template_name = 'Probe/templates/Probe_model_list.html'


class ProbeListVView(generic.ListView):
    model = ProbeList
    template_name = 'Probe/templates/Probe_list_by_model.html'