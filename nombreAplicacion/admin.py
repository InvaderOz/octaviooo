from django.contrib import admin
from .models import Marca
# Register your models here.
class MarcaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'activo']
    list_display_links = ['nombre', 'activo']
    list_filter = ['nombre', 'activo']
    search_fields = ['nombre', 'activo']
admin.site.register(Marca)