from django.shortcuts import render

def first(request):
    return render(
        request,
        'first.html'
    )

def second(request):
    return render(
        request,
        'second.html'
    )

def third_view(request, param):
    return render(
        request,
        'third.html'
    )