from django.shortcuts import render, redirect
from stringFormatter.formatter import to_upper_case
from .models import Text


def index(request):


    return render(request, 'stringFormatter/index.html')


def formatter(request):
    message = ""

    if 'q' in request.POST:
        text = Text()
        text.result = to_upper_case(request.POST['q'])
        message = text.result


    return render(request, 'stringFormatter/formatter.html', {'content': message})
