from django.shortcuts import render


def index(request):
    return render(request, 'fbInternship/index.html')


def album(request):
    return render(request, 'fbInternship/album.html', {'title': "usah"})
