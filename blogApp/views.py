
from django.shortcuts import render, get_object_or_404
from blogApp.models import BlogPost, PostAuthor, Comment, PostCategory
from cleaningApp.models import SiteSetting
from slider.models import blogSlider
from .views import *
# Create your views here.
def blog(request):
    blogs = BlogPost.objects.all()
    homeblogs = BlogPost.objects.all().order_by('-add_date')[:3]
    authimage = PostAuthor.objects.all()
    settings = SiteSetting.objects.all()
    blogslider = blogSlider.objects.all().order_by('-hslider_id')[:1]
    context = {'blogs':blogs, 'authimage':authimage, 'settings':settings, 'blogslider':blogslider, 'homeblogs':homeblogs}
    return render(request, 'blog.html', context)




def blog_detail(request, slug_url):
    blogd = BlogPost.objects.get(slug=slug_url)
    homeblogs = BlogPost.objects.all().order_by('-add_date')[:3]
    authimage = PostAuthor.objects.all()
    settings = SiteSetting.objects.all()
    blogslider = blogSlider.objects.all().order_by('-hslider_id')[:1]
    comments = Comment.objects.all()
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        website=request.POST.get('website')
        content=request.POST.get('content')
        en=Comment(name=name,email=email,website=website,content=content,)
        en.save()
    
    context ={'blogd':blogd,'homeblogs':homeblogs, 'authimage':authimage, 'settings':settings, 'blogslider':blogslider,'comments':comments,}
    return render(request, "blog-single.html", context)

    
        