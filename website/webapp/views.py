from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.views.generic import TemplateView, ListView


def home(request):
    return render(request, "home.html")


def write_to_tmp(f, title):
    with open("/tmp/" + title, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def file_upload(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)
    return render(request, 'upload.html')
