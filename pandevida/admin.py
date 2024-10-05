from django.contrib import admin
from .models import Category, Product
# Register your models here.
class categoryadmin (admin.ModelAdmin):
    list_display = ("name", "description")
    search_fields = ("name"  , "description")
    list_filter  = ("name", "description")



admin.site.register(Category,categoryadmin)