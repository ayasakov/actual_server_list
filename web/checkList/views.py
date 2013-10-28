# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response

from checkList import listServers

def index(request):
    context = RequestContext(request)
    ListServer = listServers.List()

    context_dict = {'serverList': ListServer.buildList()}

    return render_to_response('checkList/index.html', context_dict, context)