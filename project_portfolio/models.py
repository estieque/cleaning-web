from distutils.command.upload import upload
from turtle import title
from django.db import models
from django.utils.html import format_html
# Create your models here.
class Portfolio(models.Model):
    portfolio_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null=True)
    meta_description = models.CharField(max_length=80)
    meta_tags = models.CharField(max_length=200)
    descriptions = models.TextField()
    image = models.ImageField(upload_to='portfolio/')
    add_date = models.DateTimeField(auto_now_add=True, null=True)
    
    def image_tag(self):
        return format_html('<img src="/media/{}" heights="60" width="60" />'.format(self.image))
    def __str__(self):
        return self.title
        