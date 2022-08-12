from django.shortcuts import render

from blogApp.models import BlogPost
from cleaningApp.models import SiteSetting

# Create your views here.
def pricing(request):
    homeblogs = BlogPost.objects.all().order_by('-add_date')[:3]
    settings = SiteSetting.objects.all()
    context = {'settings':settings, 'homeblogs':homeblogs}
    return render(request, 'pricing.html',context)