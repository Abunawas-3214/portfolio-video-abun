from multiprocessing import context
from django.shortcuts import render


def index(request):
    return render(request, 'index.html', context)

def resume(request):
    return render(request, 'resume.html')

def contact(request):
    if request.method == 'POST':
        print("data sent")
    return render(request, 'contact.html')
