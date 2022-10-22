from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def resume(request):
    return render(request, 'resume.html')


def portfolio(request):
    return render(request, 'index.html')


def contact(request):
    if request.method == 'POST':
        print("data sent")
    return render(request, 'contact.html')
