from django.contrib import admin
from ontrack_app.models import UserProfile


#makes the pages accesible via the admin interface
class PageAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}

    
# Update the registration to include this customised interface
admin.site.register(UserProfile)
