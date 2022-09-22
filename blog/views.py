from django.views.generic import ListView, DetailView
from .models import Post
from django.shortcuts import render

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

def plantrvl(request):
    return render(
        request,
        'blog/plantrvl.html'
    )


class Forums(ListView):
    model = Post
    ordering = '-pk'
    paginate_by=5



# def blog(request):
#     posts = Post.objects.all()
#     return render(
#         request,
#         'blog/blog.html',
#     )

# def community(request, pk):
#     post = Post.objects.get(pk=pk)

#     return render(
#         request,
#         'blog/community.html',
#         {
#             'post' : post,
#         }
#     )