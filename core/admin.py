from django.contrib import admin

from core.models import MeasurementUnit, Product, Shop, Receipt, StockItem, Purchase

admin.site.site_header = "Рецепти"
admin.site.site_title = "Рецепти"
admin.site.index_title = "Вітаємо на сторінці"


@admin.register(MeasurementUnit)
class MeasurementUnitAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_name')
    search_fields = ('name', 'short_name')


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')
    search_fields = ('name', 'address')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'measurement_unit')
    search_fields = ('title',)


@admin.register(Receipt)
class ReceiptAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    search_fields = ('title', 'description')


class StockItemsInline(admin.TabularInline):
    model = StockItem
    extra = 1


@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('date', 'total_price')
    search_fields = ('date', 'total_price')
    inlines = [StockItemsInline]
