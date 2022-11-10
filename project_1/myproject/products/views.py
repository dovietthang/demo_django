from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    print('123')
    return render(request, template_name='index.html', context={
        'name':'Products'
    })
