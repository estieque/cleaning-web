from multiprocessing import context
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse
from project_portfolio.models import Portfolio
from slider.models import homeSlider

from teamMembers.models import TeamMember
from testimonial.admin import TestimonialAdmin
from testimonial.models import Testimonial
from project_portfolio.models import Portfolio
from .models import *
from blogApp.models import *
# Create your views here.
def home(request):
    settings = SiteSetting.objects.all()
    authimage = PostAuthor.objects.all()
    homeblogs = BlogPost.objects.all().order_by('-add_date')[:3]
    team = TeamMember.objects.all().order_by('-member_id')[:3]
    testimonial = Testimonial.objects.all()
    portfolio = Portfolio.objects.all().order_by('-add_date')[:8]
    hslider = homeSlider.objects.all().order_by('-hslider_id')[:1]
    if request.method=="POST":
        name=request.POST.get('name')
        phone=request.POST.get('phone')
        service=request.POST.get('service')
        member=request.POST.get('member')
        en=Apointment(name=name,phone=phone,service=service,member=member,)
        en.save()
    context = {'settings':settings,'homeblogs':homeblogs, 'authimage':authimage,'team':team, 'testimonial':testimonial, 'portfolio':portfolio, 'hslider':hslider}
    return render(request, 'home.html', context)

        