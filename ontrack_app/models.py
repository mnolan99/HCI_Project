from django.db import models
from django.contrib import admin
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class PageAdmin(admin.ModelAdmin):
    list_display = ('title')

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    #def __str__(self):
      #  return self.user.username(editable=True)
