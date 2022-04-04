from django.shortcuts import render


def gallery(request):
    return render(request, 'gallery/gallery.html')


def viewImage(request, pk):
    return render(request, 'gallery/image.html')


def addImage(request):
    return render(request, 'gallery/add.html')