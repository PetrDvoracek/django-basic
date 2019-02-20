from django.shortcuts import render


def index(request):
    return render(request, 'index.html', {'stuff' :
        str(request.META['HTTP_AUTHORIZATION'])})
