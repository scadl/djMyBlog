from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings

from .models import *
from .forms import PostForm


# Create your views here.
def base():
    try:
        postPaged = Post.objects.filter(category__isnull=True);
    except Post.DoesNotExist:
        postPaged = None

    print(postPaged)

    header = {
        'theSections': Sections.objects.all(),
        'thePages': postPaged,
        'theTitle': settings.SITE_TITLE
    }

    return header


def index(request):
    try:
        postPinned = Post.objects.filter(pinn=True);
    except Post.DoesNotExist:
        postPinned = None;

    thePress = {
        'theProcla': Presentation.objects.filter(Kind=0),
        'theAdvance': Presentation.objects.filter(Kind=1),
        'thePartner': Presentation.objects.filter(Kind=2),
    }

    VContext = {
        'postPinned': postPinned,
        'thePres': thePress,
        'theHeader': base
    }

    return render(request, 'index.html', VContext)


def post_list(request):
    # "-" is ORDER BY ASC
    posts = Post.objects.order_by('-published_date')
    return render(request, 'arts.html', {'posts_list': posts, 'glo_settings': base})


def post_detail(request, auk):
    # Failsafe version of:
    # post = Post.object.get(pk=pk)
    post_this = get_object_or_404(Post, alias=auk)
    return render(request, 'apps.html', {'post': post_this, 'glo_settings': base})


TPLS = {
    'img': 'arts.html',
    'cat': 'apps.html',
};


def section(request, auk):

    thePosts = None
    tpl = 'na.html'

    #try:
    Ali = Sections.objects.get(Alias=auk)
    theCats = Category.objects.filter(Section=Ali.pk)
    thePosts = Post.objects.filter(category__in=theCats)
    tpl = TPLS[Ali.Kind]
    #except:
    #    tpl = 'na.html'
    #    theCats = None

    vcont = {
        'theHeader': base,
        'theCats': theCats,
        'thePosts': thePosts,
        'theAli': auk,
    };

    print(vcont)
    return render(request, tpl, vcont);


def page(req, auk):
    return 0