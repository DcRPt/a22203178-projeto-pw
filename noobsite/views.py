# noobsite/views.py

from django.http import HttpResponse

def index_view(request):
    return HttpResponse("Olá n00b, esta é a página web mais básica do mundo!")

def about_view(request):
    return HttpResponse("Esta é a página 'Sobre' do noobsite. Aqui não há muito para dizer!")

def contact_view(request):
    return HttpResponse("Pode entrar em contato conosco através do endereço de e-mail: contato@noobsite.com")

def services_view(request):
    return HttpResponse("Não estamos a prestar serviços neste momento.")