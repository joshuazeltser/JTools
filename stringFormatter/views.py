from django.shortcuts import render
from django.http import HttpResponse
from .models import Text
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.core.exceptions import *

# Create your views here.

def index(request):
    return render(request, 'stringFormatter/details.html')

def details(request):
    if 'q' in request.POST:
        message = 'You searched for: %r' % request.POST['q']
    else:
        message = 'You submitted an empty form.'
    return render(request, 'stringFormatter/text.html')

def text(request):

    HttpResponse("This is the result of your requested string formatting %s" )

def result(request, text_id):
    return HttpResponse("This is the result of your requested string formatting %s" % text_id)
