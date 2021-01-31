from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView
# Create your views here.
from myapp.models import Post


def home(request):

    posts = Post.objects.all()
    context = {

        'posts': posts
    }

    return render(request, 'pages/home_page01.html', context )

# def views(request):
#     view = Post.object.getId.all()
#     context = {
#
#         'view': view
#     }
#
#     return render(request, 'pages/view_page01.html',  context)

class HomeDetailView(DetailView):
    model = Post
    template_name = 'pages/detail.html'