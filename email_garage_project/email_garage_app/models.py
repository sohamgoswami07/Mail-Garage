from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from cloudinary.uploader import upload

# Create your models here.
class BrandDetail(models.Model):
    brand_name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    brand_type = models.CharField(max_length=50)
    brand_url = models.CharField(max_length=100)
    brand_about = models.CharField(max_length=500)
    brand_differenciator = models.CharField(max_length=500, null=True, blank=True)
    brand_email = models.CharField(max_length=500, null=True, blank=True)
    brand_logo = CloudinaryField('image')
    brand_strategy_img = CloudinaryField('image')
        
    def __str__(self):
        return self.brand_name

class EmailDetail(models.Model):
    connected_brand = models.ForeignKey(BrandDetail, on_delete=models.CASCADE, related_name='connected_brand', blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    email_subject = models.CharField(max_length=150)
    email_category = models.CharField(max_length=50)
    email_type = models.CharField(max_length=50)
    email_body = CloudinaryField('image')
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.email_subject

class TemplatesDetail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    template_subject = models.CharField(max_length=150)
    template_creation_tool = models.CharField(max_length=50)
    template_header_img = CloudinaryField('image')
    template_link = models.CharField(max_length=150)
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.template_subject

class BlogDetail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    blog_title = models.CharField(max_length=100)
    blog_body = CloudinaryField('raw')
    blog_header_img = CloudinaryField('image')
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.blog_title

    def save(self, *args, **kwargs):
        # If blog_body is a new upload and not yet a URL
        if self.blog_body and not str(self.blog_body).startswith("http"):
            upload_result = upload(
                self.blog_body,
                resource_type='raw'
            )
            self.blog_body = upload_result['url']
        
        super().save(*args, **kwargs)