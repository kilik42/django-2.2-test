from django.http import HttpResponse


def home_page(request):
    return HttpResponse("<h1> helo world</h1>")

def about_page(request):
    return HttpResponse("<h1> about</h1>")

def contact_page(request):
    return HttpResponse("<h1> contact</h1>")
