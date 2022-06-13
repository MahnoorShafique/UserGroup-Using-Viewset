from django.contrib import admin

# Register your models here.
from user.models import ProfileFeedItem, UserProfile, UserProfileManager

admin.site.register(ProfileFeedItem)
admin.site.register(UserProfile)
