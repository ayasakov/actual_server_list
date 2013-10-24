# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response

def index(request):
    context = RequestContext(request)
    context_dict = {'boldmessage': "I am from the context"}

    return render_to_response('checkList/index.html', context_dict, context)