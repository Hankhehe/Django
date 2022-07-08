from django.shortcuts import render
from django.views import generic
from .models import ProbeModelDetail,ProbeList
# Create your views here.

def ProbeDashboard(request):
    P110Count = ProbeList.objects.filter(ModelID=6).count()
    P110PlusCount = ProbeList.objects.filter(ModelID=3).count()
    P220Count = ProbeList.objects.filter(ModelID=4).count()
    P360Count = ProbeList.objects.filter(ModelID=5).count()
    P500Count = ProbeList.objects.filter(ModelID=7).count()
    return render(request,'Probe/templates/Probe_DashBoard.html'
    ,{'P110':P110Count,'P110Plus':P110PlusCount,'P220':P220Count,'P360':P360Count,'P560':P500Count}) 

class ProbeModelListView(generic.ListView):
    model = ProbeModelDetail
    template_name = 'Probe/templates/Probe_model_list.html'

class ProbeListVView(generic.ListView):
    model = ProbeList
    template_name = 'Probe/templates/Probe_device_list.html'