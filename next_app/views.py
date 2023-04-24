from django.shortcuts import render, HttpResponse
from django.utils.html import escape

# Create your views here.

def hello(request):
    return HttpResponse("Hello World!")

def eva(request):
    return HttpResponse("Hello <span style='color:red'>Eva</span>!")

def adam(request):
    return HttpResponse("Hello Adam!")

def name(request, data):
    # podatność xss
    # Xss - cross site scripting

    # always remember to escape your output
    print(data)
    escaped_data = escape(data)# dzięki temu escape blokujemy/zabezpieczamy dostęp do ściezki przed hakerami i zmianami
    print(escaped_data)
    return HttpResponse(f"Hello, {escaped_data}!")