from django.shortcuts import render

# Create your views here.
def first_view(request):
    return render(
        request,
        'first_template.html'
    )

def second_view(request):
    return render(
        request,
        'second_template.html'
    )