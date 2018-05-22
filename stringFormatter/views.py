from django.shortcuts import render
from django.http import HttpResponse
from .models import Text
from django.shortcuts import get_object_or_404

# Create your views here.

def index(request):
    previous_strings_list = Text.objects.order_by('-text_id')

    context = {'previous_strings_list': previous_strings_list}
    return render(request, 'stringFormatter/index.html', context)

def details(request, text_id):
    text = get_object_or_404(Text, pk=text_id)

    return render(request, 'stringFormatter/detail.html', {'text': text})

def text(request, text_id):
    return HttpResponse("This is the string that you want to be formatted %s." % text_id)


def result(request, text_id):
    return HttpResponse("This is the result of your requested string formatting %s" % text_id)
