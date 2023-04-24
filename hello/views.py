from django.shortcuts import HttpResponse
from django.shortcuts import render

# Create your views here.

def hello(request):
    return HttpResponse("Hello World!")

def welcome(request):
    return HttpResponse("<h2 style='color:purple'> Cześć <span style='color:red'>Milena<span></h2>")

def hi(request):
    return HttpResponse("""<!DOCTYPE html>
    <html lang='en'>
    <head>
    <meta charset='UTF-8'>
    <title>Witaj hi</title>
    </head>
    <body>
    
    </body>
    </html>""")

def hi2(request):
    return render(request, 'hi.html')