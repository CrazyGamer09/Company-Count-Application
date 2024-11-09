from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import FileUploadForm
from .models import UploadedFile

def upload_file(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'File uploaded successfully!')
            return redirect('upload')
    else:
        form = FileUploadForm()
    return render(request, 'company/upload.html', {'form': form})

