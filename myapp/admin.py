from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Category, Invention

admin.site.register(Category)
admin.site.register(Invention)

