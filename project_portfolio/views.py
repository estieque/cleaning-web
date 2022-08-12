from django.shortcuts import render
from blogApp.models import BlogPost
from cleaningApp.models import SiteSetting

from project_portfolio.models import Portfolio
from slider.models import portfolioSlider

# Create your views here.
def portfolio(request):
    portfolio = Portfolio.objects.all()
    settings = SiteSetting.objects.all()
    homeblogs = BlogPost.objects.all().order_by('-add_date')[:3]
    portslider = portfolioSlider.objects.all().order_by('-hslider_id')[:1]
    context = {'portfolio':portfolio, 'settings':settings, 'homeblogs':homeblogs, 'portslider':portslider}
    return render(request, 'portfolio.html', context)



def port_detail(request, slug_url):
    portd = Portfolio.objects.get(slug=slug_url)
    homeblogs = BlogPost.objects.all().order_by('-add_date')[:3]
    settings = SiteSetting.objects.all()
    portslider = portfolioSlider.objects.all().order_by('-hslider_id')[:1]
    context ={'portd':portd,'homeblogs':homeblogs, 'settings':settings, 'portslider':portslider,}
    return render(request, "port-single.html", context)