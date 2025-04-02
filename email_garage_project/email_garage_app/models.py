from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class BrandDetail(models.Model):
    brand_name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    brand_type = models.CharField(max_length=50)
    brand_url = models.CharField(max_length=100)
    brand_about = models.CharField(max_length=500)
    brand_differenciator = models.CharField(max_length=500, null=True, blank=True)
    brand_email = models.CharField(max_length=500, null=True, blank=True)
    brand_logo = models.ImageField(upload_to='brand_logo/')
    brand_strategy_img = models.ImageField(upload_to='brand_strategy_img/')
        
    def __str__(self):
        return self.brand_name

class EmailDetail(models.Model):
    connected_brand = models.ForeignKey(BrandDetail, on_delete=models.CASCADE, related_name='connected_brand', blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    email_subject = models.CharField(max_length=150)
    email_category = models.CharField(max_length=50)
    email_type = models.CharField(max_length=50)
    email_body = models.FileField(upload_to='email_body/')
    date_added = models.DateTimeField(default=timezone.now)
        
    def __str__(self):
        return self.email_subject

class TemplatesDetail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    template_subject = models.CharField(max_length=150)
    template_creation_tool = models.CharField(max_length=50)
    template_link = models.CharField(max_length=150)
    date_added = models.DateTimeField(default=timezone.now)
        
    def __str__(self):
        return self.template_subject

class BlogDetail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    blog_title = models.CharField(max_length=100)
    blog_body = models.FileField(upload_to='blog_body/')
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.blog_title