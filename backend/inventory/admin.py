from django.contrib import admin
from inventory.models import Category, Product, Report

class CategoryAdmin(admin.ModelAdmin):
    list_category = ('type')

class ProductAdmin(admin.ModelAdmin):
    list_product = ('code', 'name', 'quantity', 'price', 'category')

class ReportAdmin(admin.ModelAdmin):
    list_report = ('product_id', 'quantity_add', 'stockleft')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Report, ReportAdmin)
