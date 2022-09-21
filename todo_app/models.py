from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.urls import reverse
# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=200)
    slug = models.SlugField(null=False)
    description = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

    


    def get_absolute_url(self):
        return reverse("update", kwargs={"slug": self.slug})
    
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


    def get_absolute_urls(self):
        return reverse("delete", kwargs={"slug": self.slug})    
    
    class Meta:
        ordering = ['-created_at']
        
class Profile(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=200)
    profile_picture = models.FileField(upload_to="static/images/profile_picture/", blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

