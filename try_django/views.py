from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template


def home_page(request):
    my_title="hello there"

    context = {"title": my_title, "my_list": [1,2,3,4,5]}
    return render(request, "home.html",context )

def about_page(request):
    return render(request, "about.html",{"title": "About"})

def contact_page(request):
    return render(request, "contact.html",{"title": "contact"})

def example_page(request):
    context = {"title": "Example"}
    template_name = "hello_world.html"
    template_obj = get_template(template_name)
    return HttpResponse(template_obj.render(context))