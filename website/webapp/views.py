from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm
from django.core.files.storage import FileSystemStorage


def home(request):
    return render(request, "home.html")


def css_main(request):
    return render(request, "css/main.css")


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
