from django.shortcuts import render

def index(request):
    return render(request, 'home/home_index.html', {})
