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
    message5 = request.POST.get('input5', '')
    message6 = request.POST.get('input6', '')
    message7 = request.POST.get('input7', '')
    message8 = request.POST.get('input8', '')
    message9 = request.POST.get('input9', '')

    if 'lower' in request.POST:
        message2 = Text.to_lower_case(message)
    elif 'upper' in request.POST:
        message2 = Text.to_upper_case(message)
    elif 'word' in request.POST:
        print(message3)
        message4 = Text.word_count(message3)
    elif 'char' in request.POST:
        message4 = Text.char_count(message3)
    elif 'split' in request.POST:
        message6 = Text.split_string_by(message5, message7)
    elif 'count' in request.POST:
        message9 = Text.word_occurence_count(message8)

    print(request.POST)

    return render(request, 'stringFormatter/formatter.html', {'content': message, 'content2': message2,
                                                              'content3': message3, 'content4': message4,
                                                              'content5': message5, 'content6': message6,
                                                              'content7': message7, 'content8': message8,
                                                              'content9': message9})

def about(request):
    return render(request, 'stringFormatter/about.html')

def randomiser(request):
    return render(request, 'stringFormatter/randomiser.html')

def pdfeditor(request):
    return render(request, 'stringFormatter/pdfeditor.html')