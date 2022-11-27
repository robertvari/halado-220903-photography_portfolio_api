from django.shortcuts import render

# Create your views here.
def home_view(request):
    context = {
        "name": "Robert Vari",
        "subtitle": "photography"
    }

    return render(request, "home.html", context)


def about_view(request):
    return render(request, "about.html")


def contact_view(request):
    return render(request, "contact.html")


def gallery_view(request):
    return render(request, "gallery.html")