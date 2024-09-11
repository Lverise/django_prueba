from django.shortcuts import render

# Create your views here.

def menuTemplate(render):
    return(render, '/Listado/index.html')

def pagina2Template(render):
    return(render, '/Listado/pagina2.html')