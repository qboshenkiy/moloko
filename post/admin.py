from django.contrib import admin
from .models import productAdd
# Register your models here.

@admin.register(productAdd)
class productAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'text')
