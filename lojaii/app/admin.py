from django.contrib import admin

#Importing all models from app/models.py
from .models import *

# Register your models he

class ProdutoInline(admin.TabularInline):
    model = Produto
    extra = 1

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome']
    search_fields = ['nome']
    inlines = [ProdutoInline]

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'preco', 'categoria']
    search_fields = ['nome']
    list_filter = ['categoria']

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Produto, ProdutoAdmin)