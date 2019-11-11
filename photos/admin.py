from django.contrib import admin
from .models import Image,Photo,Location

# Register your models here.
class PhotoAdmin(admin.ModelAdmin):
    filter_horizontal =('location',)

admin.site.register(Image)
admin.site.register(Photo,PhotoAdmin)
admin.site.register(Location)

