from django.http import Http404
from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import BlogPost





def blog_post_detail_page(request, slug):
    queryset = BlogPost.objects.filter(slug = slug)
    if queryset.count() == 0:
        obj = queryset.first()
    else:
        raise Http404



    #obj = get_object_or_404(BlogPost, slug=slug)
    # try:
    #     obj = BlogPost.objects.get(id=id)
    # except BlogPost.DoesNotExist:
    #     raise Http404
    # except ValueError:
    #     raise Http404
    template_name = 'blog_post_detail.html'
    context = {"object":obj}

    return render(request, template_name, context)