from django.shortcuts import render
from blogApp.models import BlogPost

from cleaningApp.models import SiteSetting
from project_portfolio.models import Portfolio
from slider.models import aboutSlider
from teamMembers.models import TeamMember
from testimonial.models import Testimonial

# Create your views here.
def about(request):
    settings = SiteSetting.objects.all()
    team = TeamMember.objects.all()
    testimonial = Testimonial.objects.all()
    portfolio = Portfolio.objects.all()
    homeblogs = BlogPost.objects.all().order_by('-add_date')[:3]
    aboutslider = aboutSlider.objects.all().order_by('-hslider_id')[:1]
    context = {'settings':settings, 'team':team, 'testimonial':testimonial, 'portfolio':portfolio, 'homeblogs':homeblogs, 'aboutslider':aboutslider}
    return render(request, 'about.html',context)