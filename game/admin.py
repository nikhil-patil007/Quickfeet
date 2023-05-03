from django.contrib import admin
from .models import *

# Register your models here.

class GameAdmin(admin.ModelAdmin):
    list_per_page = 15
    list_display = ('id','Via','Full_name','Game_name','Email','DOB','age','Gender','Country','Shirt_num','Is_active','Otp')
    list_display_links = ('id','Via','Full_name','Game_name','Email','DOB','age','Gender','Country','Shirt_num','Is_active','Otp')
    ordering = ('-id'),

admin.site.register(Game_user,GameAdmin)
admin.site.register(Post)
admin.site.register(Contact_Us)
admin.site.register(Contact_Us_reply)
admin.site.register(Add_Players)
admin.site.register(Drills)
admin.site.register(Drill_Formula)
admin.site.register(Drill_Data)
admin.site.register(LeaderBoard)
admin.site.register(Scorebord)
admin.site.register(Country_codes)
