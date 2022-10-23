from django.contrib import admin
from .models import Resident,Leader,Notification,Posts,Comment


class ResidentAdmin(admin.ModelAdmin):
    list_display=('first_name','last_name','county','password','neighbourhood_associattion','username')
    search_fields=('first_name','last_name','county','password','neighbourhood_associattion','username')
admin.site.register(Resident,ResidentAdmin)



class PostsAdmin(admin.ModelAdmin):
    list_display=('tittle','description','sector','image','video','time_date')
    search_fields=('tittle','description','sector','image','video','time_date')
admin.site.register(Posts,PostsAdmin)


class LeaderAdmin(admin.ModelAdmin):
    list_display=('first_name','last_name','county','password','neighbourhood_associattion','username')
    search_fields=('first_name','last_name','county','password','neighbourhood_associattion','username')
admin.site.register(Leader,LeaderAdmin)

class NotificationAdmin(admin.ModelAdmin):
    list_display=('neighbourhood','date_of_meeting','tittle_of_meeting','status')
    search_fields=('neighbourhood','date_of_meeting','tittle_of_meeting','status')
admin.site.register(Notification,NotificationAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display=('head','description','action','sector','time_date')
    search_fields=('tittle','description','sector''time_date',)
admin.site.register(Comment,CommentAdmin)
