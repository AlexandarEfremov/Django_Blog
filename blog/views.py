from django.http import HttpResponse
from django.shortcuts import render


def starting_page(request):
    return render(request, "blog/index.html")


def posts(request):
    return render(request, "blog/all-posts.html")


def post_detail(request, slug): #we need to add the slug parameter as it's a dynamic value
    return render(request, "blog/post-detail.html")

