from django.db import models

# Create your models here.
class EmailSub(models.Model):
    sub_id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=100, null=True)
    add_date = models.DateTimeField(auto_now_add=True, null=True)
    
    
    def __str__(self):
        return str(self.email)