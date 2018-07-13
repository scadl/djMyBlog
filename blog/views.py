from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
from .models import Post
from .models import Setting
from .forms import PostForm


# Create your views here.
def base():
    active_settings = Setting.objects.get(Is_Active=True)
    #active_settings['media'] = settings.MEDIA_URL
    return active_settings

def index(request):
    try:
        active_settings = Setting.objects.get(Is_Active=True)
    except ObjectDoesNotExist:
        return render(request, 'blog/na_settings.html')
    return render(request, 'blog/index_page.html', {'index_settings': active_settings, 'glo_settings': base})


def post_list(request):
    # "-" is ORDER BY ASC
    posts = Post.objects.order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts_list':posts, 'glo_settings': base})


def post_detail(request, auk):
    # Failsafe version of:
    # post = Post.object.get(pk=pk)
    post_this = get_object_or_404(Post, alias=auk)
    return render(request, 'blog/post_detail.html', {'post':post_this, 'glo_settings': base})