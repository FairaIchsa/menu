from django.shortcuts import render


def index(request, pk):
    print(request)
    context = {'pk': pk}
    return render(request, 'base.html', context=context)
