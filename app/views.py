from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, render_to_response, get_object_or_404


# Create your views here.
from django.template import RequestContext
from app.models import Blog


def homepage(request):

    if not request.user.is_authenticated():
        return HttpResponseRedirect('/accounts/register')

    return render(request, 'default/index.html', {'entity': 'Wow'})


def register(request):
    if request.method == 'POST':
        register_form = UserCreationForm(request.POST)
        if register_form.is_valid:
            register_form.save()
            return HttpResponseRedirect('/')
    else:
        register_form = UserCreationForm()
    return render_to_response('account/register.html', {'form': register_form},
                              context_instance=RequestContext(request))


def about(request):
    return render(request, 'default/about.html', context_instance=RequestContext(request))

def contact(request):
    return render(request, 'default/contact.html', context_instance=RequestContext(request))


def do_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid:
            username = request.POST['username']
            password = request.POST['password']
            access = authenticate(username=username, password=password)
            if access is not None:
                if access.is_active:
                    login(request, access)
                    return HttpResponseRedirect('/')
                else:
                    return HttpResponseRedirect('/')
            else:
                render_to_response('default/index.html', context_instance=RequestContext(request))
    else:
        form = AuthenticationForm()
    return render_to_response('account/login.html', {'form': form}, context_instance=RequestContext(request))


def logout(request):
    auth.logout(request)
    # Redireccciona a una página de entrada correcta.
    return HttpResponseRedirect("/")

def blog_list(request):
    entities = Blog.objects.all()
    return render(request, 'blog/index.html', { 'entities': entities }, context_instance=RequestContext(request))

def blog_details(request, blog_id):
    entity = get_object_or_404(Blog, pk = blog_id)
    return render(request, 'blog/details.html', { 'entity': entity }, context_instance=RequestContext(request))
