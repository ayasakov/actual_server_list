# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import json


from checkList.forms import UserForm, UserProfileForm
from checkList import listServers


def index(request):
    context = RequestContext(request)
    context_dict = ""
    return render_to_response('checkList/index.html', context_dict, context)


def register(request):
    context = RequestContext(request)
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()

            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            profile.save()
            registered = True

        else:
            print user_form.errors, profile_form.errors

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render_to_response(
        'checkList/register.html',
        {
            'user_form': user_form,
            'profile_form': profile_form,
            'registered': registered
        },
        context)


def user_login(request):
    context = RequestContext(request)

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/checkList/')
            else:
                return HttpResponse("Your account is disabled.")
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    else:
        return render_to_response('checkList/login.html', {}, context)


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/checkList/')


def about(request):
    return HttpResponse("Page about this project. Comming soon...")


@login_required
def user_edit(request):
    context = RequestContext(request)
    user_profile = request.user.get_profile()

    edited = False

    if request.method == 'POST':
        profile_form = UserProfileForm(data=request.POST,
                                       instance=user_profile)

        if profile_form.is_valid():
            profile_form.save()
            edited = True

        else:
            print profile_form.errors

    else:
        profile_form = UserProfileForm()

    return render_to_response(
        'checkList/edit.html',
        {'profile_form': profile_form, 'edited': edited},
        context)


@login_required
def list(request):
    context = RequestContext(request)

    user = context['user']
    context_dict = ""

    if user.is_active:
        profile = user.get_profile()
        ListServer = listServers.List(profile.login_nova,
                                      profile.password_nova,
                                      profile.project_id,
                                      profile.auth_url)
        context_dict = ListServer.buildList()

    return HttpResponse(json.dumps(context_dict),
                        content_type="application/json")
