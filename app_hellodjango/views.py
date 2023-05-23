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
    dados = {'eventos':Evento}
    return render(request, 'agenda.html', dados)

@login_required(login_url='/login/')
def Evento(request):
    id_evento = request.GET.get('id')
    dados = {}
    if id_evento:
        dados['evento'] = evento.objects.get(id=id_evento)
    return render(request,'evento.html', dados)


@login_required(login_url='/login/')
def submit_evento(request):
    if request.POST:
        titulo = request.POST.get('titulo')
        data_evento = request.POST.get('data_evento')
        descricao = request.POST.get('descricao')
        usuario = request.user
        id_evento = request.POST.get("id_evento")
        if id_evento:
            Evento = evento.objects.get(id=id_evento)
            if Evento.usuario == usuario:
                Evento.titulo = titulo
                Evento.descricao = descricao
                Evento.data_evento = data_evento
                Evento.save()
            # evento.objects.filter(id=id_evento).update(titulo=titulo,
            #                                             data_evento=data_evento,
            #                                             descricao=descricao)
        else:
            evento.objects.create(titulo=titulo,
                              data_evento=data_evento,
                              descricao=descricao,
                              usuario=usuario)
    return redirect('/')

@login_required(login_url='/login/')
def delete_evento(request, id_evento):
    usuario = request.user
    Evento = evento.objects.get(id=id_evento)
    if usuario == Evento.usuario:
        Evento.delete()
    return redirect('/') 
    
    


    
   