from django.shortcuts import render
from .models import Image
from .form import ImageForm



# Create your views here.

def gallery(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return HttpResponse('successfully uploaded')
    else:
        form = ImageForm()
    return render(request, "gallery/gallery.html", {"form": form})