import email
from unicodedata import name
from django.shortcuts import render
from django.core.mail import send_mail
from blogApp.models import BlogPost

from cleaningApp.models import SiteSetting
from .models import EmailSub
from slider.models import contactSlider
# Create your views here.
def contact(request):
     settings = SiteSetting.objects.all()
     homeblogs = BlogPost.objects.all().order_by('-add_date')[:3]
     contslider = contactSlider.objects.all().order_by('-hslider_id')[:1]
     context = {'settings':settings,'homeblogs':homeblogs, 'contslider':contslider}
     if request.method=="POST":
          email=request.POST.get('email')
          en=EmailSub(email=email,)
          en.save()
     if request.method == "POST":
         contact_name = request.POST['contact-name']
         contact_email = request.POST['contact-email']
         contact_subject = request.POST['contact-subject']
         message = request.POST['message']
         
         #send mail option
         send_mail(contact_name, message, contact_email, ['estiequealam6815@gmail.com'])
         context = {'contact_name': contact_name,}
         return render(request, 'contact.html', context,)
     else:
        return render(request, 'contact.html', context)