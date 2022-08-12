from email import message
from django.db import models
from django.utils.html import format_html
# Create your models here.
class Testimonial(models.Model):
    testimonial_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=150)
    email = models.EmailField(blank=True, null=True, max_length=50)
    image = models.ImageField(blank=True, null=True, upload_to='teamimage/')
    message = models.TextField()
    
    def image_tag(self):
        return format_html('<img src="/media/{}" heights="60" width="60" />'.format(self.image))
    
    def __str__(self):
        return self.name