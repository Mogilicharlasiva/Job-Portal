from django.shortcuts import render
from django.http import HttpResponse
from .models import JobPost
from django.views.generic import ListView, DetailView
# Create your views here.

def home(request):
    jobs_list = JobPost.objects.order_by("-pub_date")
    context = {"jobs_list":jobs_list}
    return render(request, 'job_listings/home.html', context)

class DetailPostView(DetailView):
    model = JobPost
    template_name = 'job_listings/jobpost.html'
    context_object_name = 'jobpost'
    ordering = '-pub_date'