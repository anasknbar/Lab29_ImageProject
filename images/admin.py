from django.contrib import admin
from .models import Image
# Register your models here.

class ImageAdmin(admin.ModelAdmin):
  list_display = ("image_type","tag","webformatURL","views","downloads","likes","user","userimageURL")
admin.site.register(Image,ImageAdmin)