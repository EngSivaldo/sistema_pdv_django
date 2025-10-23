from django.contrib import admin
from .models import Venda, ItemVenda

class ItemVendaInline(admin.TabularInline):
    model = ItemVenda
    extra = 1

class VendaAdmin(admin.ModelAdmin):
    inlines = [ItemVendaInline]
    list_display = ('id', 'cliente', 'data', 'total')

admin.site.register(Venda, VendaAdmin)
