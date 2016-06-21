from django.contrib import admin
from imageline.models import photo

# Register your models here.
class photoAdmin(admin.ModelAdmin):
    list_display  =  ('program','publicFlag',)


admin.site.register(photo,photoAdmin)

