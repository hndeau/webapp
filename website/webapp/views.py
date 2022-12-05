import os
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage


def home(request):
    return render(request, "home.html")


def write_to_tmp(f, title):
    with open("/tmp/" + title, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def file_upload(request):
    if request.method == 'POST' and request.FILES.__len__():
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        fs.save(uploaded_file.name.replace(" ", "_"), uploaded_file)
    return render(request, 'upload.html')


def file_search(request):
    if request.method == 'POST':
        query = request.POST['query']
        result = None
        url = 'http://'
        if query:
            # we split this by colon to just obtain the hostname
            hostname = request.get_host().split(':')[0]
            # Construct the new url to redirect to
            url += hostname + ':' + '8080' + '/media/'
            result = os.popen(
                "cd media && find . -type f -iname '*" + query + "*'").read().split()  # TODO implement library file search
        return render(request, 'search.html', {'query': result, 'url': url})
    else:
        return render(request, 'search.html', {'query': None})
