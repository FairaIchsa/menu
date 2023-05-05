from django.shortcuts import render


def index(request, pk):
    context = {'pk': pk}
    return render(request, 'base.html', context=context)
