from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.urls import revers
from django.views import generic

from .models import Partner

# Create your views here.

def index(request):
    return render(request, 'partner/index.html')

# To be implemented:
# class IndexView(generic.ListView):
#     model = Partner
#     template_name = "partner/index.html"

# class DetailView(generic.DetailView):
#     model = Partner
#     template_name = "partner/detail.html"

# class ResultsView(generic.DetaiView):
#     model = Partner
#     template_name = "partner/results.html"
