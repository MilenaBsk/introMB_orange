from datetime import datetime

from django.shortcuts import render, HttpResponse
from django.utils.html import escape


# Create your views here.
class Cow:
    def __init__ (self, name):
        self.name = name
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

def hello2(request):
    return render(
        request,
        'hello.html'
    )

def name2(request, data):
    return render(
        request,
        'name.html',
        context={
            "data":data
        }
    )


# widoki - warstwa logiki
# szablony - warstwa prezentacji DTL - dajngo template language
def is_it_new_year(request):
    now = datetime.now()

    is_new_year = False
    if now.day == 1 and now.month == 1:
        is_new_year = True

    return render(
        request,
        'is_it_new_year.html',
        context={
            'is_new_year': is_new_year}
    )


def fruits(request):
    fruits_list = [
        'jabłko',
        'banan',
        'winogrono',
        'mandarynki'
    ]

    person = {
        "name": "Jan",
        "surname": "Kowalski",
        "age": 35,
    }

    cow = Cow(name="Mućka")

    return render(
        request,
        'fruits.html',
        context={
            'fruits': fruits_list,
            'person': person,
            'cow': cow,
        }
    )