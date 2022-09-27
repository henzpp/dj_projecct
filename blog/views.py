from django.views.generic import ListView, DetailView
from .models import Post
from django.shortcuts import render
import re


class PostList(ListView):
    model = Post
    ordering = '-pk'

class PostDetail(DetailView):
    model = Post



def community(request):
    return render(
        request,
        'blog/community.html'
    )

def forums(request):
    return render(
        request,
        'blog/forums.html'
    )

def gallery(request):
    return render(
        request,
        'blog/gallery.html'
    )

def places(request):
    return render(
        request,
        'blog/places.html'
    )


def forums_result(request):
    return render(
        request,
        'blog/forums_result.html'
    )

def forums_result2(request):
    return render(
        request,
        'blog/forums_result2.html'
    )

def forums_result3(request):
    return render(
        request,
        'blog/forums_result3.html'
    )

def forums_result4(request):
    return render(
        request,
        'blog/forums_result4.html'
    )



class Forums(ListView):
    model = Post
    ordering = '-pk'
    paginate_by=5






def inputdata(request):
    return render(request, 'blog/forums.html')

def result(request):

    res = request.GET(['A'])
    l = int(res)


    if 0 < l < 100:
        return render(request, 'blog/forums_result.html')
    elif 100 <=  l < 300:
        return render(request, 'blog/forums_result2.html')
    elif 300 <= l < 500 :
        return render(request, 'blog/forums_result3.html')
    elif 899999 < l <= 1000000 :
        return render(request, 'blog/forums_result4.html')
