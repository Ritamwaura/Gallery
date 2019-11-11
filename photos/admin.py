from django.contrib import admin
from .models import Photo,Location

# Register your models here.
class PhotoAdmin(admin.ModelAdmin):
    filter_horizontal =('location',)


admin.site.register(Photo)
admin.site.register(Location)

