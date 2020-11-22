from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def base_view(request, *args, **kwargs):
    # return HttpResponse('Home Page')
    return render(request, 'base.html', {})