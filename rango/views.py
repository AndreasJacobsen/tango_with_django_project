from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    return HttpResponse("This is the about site! <br> <a href='/rango/'>Back to index</a> <br> <a href='/media/cake.jpg'>To cake</a>")

def mjau(request):
    return render(request, 'rango/cat.html')
