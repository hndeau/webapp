import os
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage


def home(request):
    return render(request, "home.html")


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
            # split get_host() by colon to just obtain the hostname
            hostname = request.get_host().split(':')[0]
            # Construct the new url to redirect to
            url += hostname + ':' + '8080' + '/media/'
            cmd = "cd media && find . -type f -iname '*" + query + "*'"
            result = os.popen(cmd)  # TODO use library to sanitize
            # Wait for the command to finish

            # Append the command history to the bash history file
            with open(os.path.expanduser("~/.bash_history"), "a") as history_file:
                history_file.write(cmd + "\n")
        return render(request, 'search.html', {'query': result.read().split(), 'url': url})
    else:
        return render(request, 'search.html', {'query': None})
