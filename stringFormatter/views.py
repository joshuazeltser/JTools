from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Text


def index(request):
    return render(request, 'stringFormatter/index.html')


def formatter(request):

    message = request.POST.get('input1', '')
    message2 = request.POST.get('input2','')
    message3 = request.POST.get('input3', '')
    message4 = request.POST.get('input4', '')

    if 'lower' in request.POST:
        message2 = Text.to_lower_case(message)
    elif 'upper' in request.POST:
        message2 = Text.to_upper_case(message)
    elif 'word' in request.POST:
        message4 = Text.word_count(message3)
    elif 'char' in request.POST:
        message4 = Text.char_count(message3)

    print(request.POST)

    return render(request, 'stringFormatter/formatter.html', {'content': message, 'content2': message2,
                                                              'content3': message3, 'content4': message4})
