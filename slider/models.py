from django.db import models
from django.utils.html import format_html
# Create your models here.
class homeSlider(models.Model):
    hslider_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    short_title = models.CharField(max_length=60, null=True)
    long_title = models.CharField(max_length=60, null=True)
    image = models.ImageField(upload_to='slideimage/')
    def image_tag(self):
        return format_html('<img src="/media/{}" heights="60" width="60" />'.format(self.image))
    def __str__(self):
        return self.name
        
class aboutSlider(models.Model):
    hslider_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='slideimage/')
    def image_tag(self):
        return format_html('<img src="/media/{}" heights="60" width="60" />'.format(self.image))
    def __str__(self):
        return self.name
    
    
class portfolioSlider(models.Model):
    hslider_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='slideimage/')
    def image_tag(self):
        return format_html('<img src="/media/{}" heights="60" width="60" />'.format(self.image))
    def __str__(self):
        return self.name
    
class blogSlider(models.Model):
    hslider_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='slideimage/')
    def image_tag(self):
        return format_html('<img src="/media/{}" heights="60" width="60" />'.format(self.image))
    def __str__(self):
        return self.name
    
class contactSlider(models.Model):
    hslider_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='slideimage/')
    def image_tag(self):
        return format_html('<img src="/media/{}" heights="60" width="60" />'.format(self.image))
    def __str__(self):
        return self.name