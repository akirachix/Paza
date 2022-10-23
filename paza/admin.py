from django.contrib import admin
from .models import Resident,Leader,Notification,Posts


class ResidentAdmin(admin.ModelAdmin):
    list_display=('first_name','last_name',)
    search_fields=("first_name","last_name",)
admin.site.register(Resident,ResidentAdmin)



class PostsAdmin(admin.ModelAdmin):
    list_display=('tittle','description','sector')
    search_fields=("tittle","description","sector")
admin.site.register(Posts,PostsAdmin)

# class LoginAdmin(admin.ModelAdmin):
#     list_display=('user_name','password')
#     search_fields=('user_name','password')
# admin.site.register(Login,LoginAdmin)

class LeaderAdmin(admin.ModelAdmin):
    list_display=('first_name','last_name','county')
    search_fields=("first_name","last_name",)
admin.site.register(Leader,LeaderAdmin)

class NotificationAdmin(admin.ModelAdmin):
    list_display=('neighbourhood','date_of_meeting','tittle_of_meeting','status')
    search_fields=("neighbourhood","date_of_meeting",'status')
admin.site.register(Notification,NotificationAdmin)

class PostsAdmin(admin.ModelAdmin):
    list_display=('tittle','description','sector')
    search_fields=("tittle","description","sector")