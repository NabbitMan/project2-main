from django.http import HttpResponse
from django.shortcuts import render

from .models import Lab

# Create your views here.
def index(request):
    lab_list = Lab.objects.all();
    context = {'lab_list': lab_list}
    return render(request, 'labs/index.html', context)

def detail(request, lab_id):
    lab = Lab.objects.get(pk=lab_id)
    context = {'lab': lab}
    return render(request, 'labs/detail.html', context)