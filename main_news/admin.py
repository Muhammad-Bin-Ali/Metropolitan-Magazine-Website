from django.contrib import admin
from .models import NewsPost, UserFeedList, FeedLink
# Register your models here.
admin.site.register(NewsPost)
admin.site.register(UserFeedList)
admin.site.register(FeedLink)