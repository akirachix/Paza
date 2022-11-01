from django.contrib import admin
from .models import Resident,Leader,Notification,Comment,Forum,Posts,Discussion


class ResidentAdmin(admin.ModelAdmin):
    list_display=('first_name','last_name','county','password')
    search_fields=('first_name','last_name','county','password')
admin.site.register(Resident,ResidentAdmin)



class PostAdmin(admin.ModelAdmin):
    list_display=('image_name','image_caption','created','image','author', 'likes')
    search_fields=('image_name','image_caption','created','image','author', 'likes')
admin.site.register(Posts,PostAdmin)


class LeaderAdmin(admin.ModelAdmin):
    list_display=('first_name','last_name','county','password','neighbourhood_associattion','username')
    search_fields=('first_name','last_name','county','password','neighbourhood_associattion','username')
admin.site.register(Leader,LeaderAdmin)

class NotificationAdmin(admin.ModelAdmin):
    list_display=('neighbourhood','date_of_meeting','tittle_of_meeting','status')
    search_fields=('neighbourhood','date_of_meeting','tittle_of_meeting','status')
admin.site.register(Notification,NotificationAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display=('body','created','post','author',)
    search_fields=('body','created','post','author',)
admin.site.register(Comment,CommentAdmin)



class ForumAdmin(admin.ModelAdmin):
    list_display=('tittle','description','date_created','topic','name')
    search_fields=('tittle','description','date_created','name')
admin.site.register(Forum,ForumAdmin)

class DiscussionAdmin(admin.ModelAdmin):
    list_display=('forum','discuss')
    search_fields=('forum','discuss')
admin.site.register(Discussion)