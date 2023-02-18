from django.shortcuts import render


def init(request):
    return render(request, 'pages/base.html')


def about(request):
    return render(request, 'pages/base.html')


