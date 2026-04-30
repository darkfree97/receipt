from django.contrib import admin

from core.models import Product, Shop, Receipt, StockItem, Purchase, ReceiptProduct, ReceiptStep

admin.site.site_header = "Рецепти"
admin.site.site_title = "Рецепти"
admin.site.index_title = "Вітаємо на сторінці"


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')
    search_fields = ('name', 'address')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)


class ReceiptProductInline(admin.TabularInline):
    model = ReceiptProduct
    extra = 1


class ReceiptStepInline(admin.StackedInline):
    model = ReceiptStep
    extra = 0


@admin.register(Receipt)
class ReceiptAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    search_fields = ('title', 'description')
    inlines = [ReceiptProductInline, ReceiptStepInline]


class StockItemsInline(admin.TabularInline):
    model = StockItem
    extra = 1


@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('date', 'total_price')
    search_fields = ('date', 'total_price')
    inlines = [StockItemsInline]
