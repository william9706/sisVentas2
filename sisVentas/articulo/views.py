from django.shortcuts import render

# Create your views here.


def vista_index(request):


    return render(request, "main.html")
