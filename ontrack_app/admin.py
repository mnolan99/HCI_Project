from django.contrib import admin
from ontrack_app.models import Review, Page
from ontrack_app.models import UserProfile


#makes the reviews accessable via the admin interface
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("reviewID", "title")

#makes the pages accesible via the admin interface
class PageAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}

    
#these lines of code register review, reviewaadmin, page, pageadmin and userprofile to the admin interface
admin.site.register(Review, ReviewAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(UserProfile)
