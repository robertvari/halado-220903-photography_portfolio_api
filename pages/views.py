from django.shortcuts import render

from .models import SiteInfo, About


# Create your views here.
def home_view(request):
    data = SiteInfo.objects.all()
    context = {}
    if data:
        context = {"data": data[0]}

    return render(request, "home.html", context)


def about_view(request):
    data = About.objects.all()
    if data:
        return render(request, "about.html", {"data": data[0]})
        
    return render(request, "about.html")


def contact_view(request):
    return render(request, "contact.html")


def gallery_view(request):
    return render(request, "gallery.html")