from django.shortcuts import render

from .models import Content
# Create your views here.


def index(request):
    contents = Content.objects.all()
    context = {
        'Contents': contents,
    }

    return render(request, 'portfolio/index.html', context)
