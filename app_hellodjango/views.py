from django.shortcuts import render, redirect
from app_hellodjango.models import evento
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages 

# def hello(request,nome):
#     return HttpResponse('<h1> Hello {} </h1>'.format(nome)
# def index(request):
#     return redirect('/agenda/')

def login_user(request):
   return render(request, 'login.html')

def logout_user(request):
    logout (request)
    return redirect('/')



def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request,usuario)
            return redirect('/')
        else:
            messages.error(request,'Usuario ou senha invalidos')
    else:
        redirect('/')
    

@login_required(login_url='/login/')
def lista_eventos(request):
    # usuario = request.user
    usuario = request.user
    Evento = evento.objects.filter(usuario=usuario)    #filter(usuario=usuario)
    response = {'eventos': Evento}
    return render(request, 'agenda.html',response)

@login_required(login_url='/login/')
def Evento(request):
    return render(request, 'evento.html')


@login_required(login_url='/login/')
def submit_evento(request):
    if request.POST:
        titulo = request.POST.get('titulo')
        data_evento = request.POST.get('data_evento')
        descricao = request.POST.get('descricao')
        usuario = request.user
        evento.objects.create(titulo=titulo,
                              data_evento=data_evento,
                              descricao=descricao,
                              usuario=usuario)
    return redirect('/')
    


    
   