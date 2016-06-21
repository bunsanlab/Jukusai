from django.contrib import admin
from program.models import program,place,vote
# Register your models here.

class programAdmin(admin.ModelAdmin):
    list_display  =  ('groupName','contentName','category','updated_at',)

class placeAdmin(admin.ModelAdmin):
    list_display  =  ('placeName','room',)

    def program(self,obj):
        return obj.program.contentName

class voteAdmin(admin.ModelAdmin):
    list_display  =  ('program',)
    search_fields =  ['program__contentName']

    def program(self,obj):
        return obj.program.contentName

admin.site.register(program,programAdmin)
admin.site.register(place,placeAdmin)
admin.site.register(vote,voteAdmin)






