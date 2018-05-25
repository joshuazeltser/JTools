from django.shortcuts import render, redirect
from stringFormatter.formatter import to_upper_case
from .models import Text


def index(request):


    return render(request, 'stringFormatter/index.html')


def formatter(request):
    message = ""
    original = ""

    if 'one' in request.POST:
        print('djksakjsadkjsadkjsadhhdask')



    if 'q' in request.POST:
        original = request.POST['q']
        text = Text()
        text.result = to_upper_case(original)
        message = text.result





    return render(request, 'stringFormatter/formatter.html', {'content': original, 'content2': message})
