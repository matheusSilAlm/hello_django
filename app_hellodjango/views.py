from django.shortcuts import render, redirect
from app_hellodjango.models import evento

# Create your views here.
# def hello(request,nome):
    
#     return HttpResponse('<h1> Hello {} </h1>'.format(nome)
# def index(request):
#     return redirect('/agenda/')

def lista_eventos(request):
    # usuario = request.user
    Evento = evento.objects.all()     #filter(usuario=usuario)
    response = {'eventos': Evento}
    return render(request, 'agenda.html',response)
    
   