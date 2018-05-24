from django.shortcuts import render, redirect
from stringFormatter.formatter import to_upper_case
from .models import Text


def index(request):
    if 'q' in request.POST:
        text = Text()
        text.result = to_upper_case(request.POST['q'])
        message = text.result
    else:
        message = 'You submitted an empty form.'

    return render(request, 'stringFormatter/index.html', {'content': message})


def details(request):
    return render(request, 'stringFormatter/index.html', {'content': message})
