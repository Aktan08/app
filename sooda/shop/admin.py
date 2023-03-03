from django.contrib import admin
from shop.models import (
    Category,
    Comment,
    Company,
    Gallery,
    SubCategory,
    ProductSite,
    ProductSize,
    SubSubCategory,
)
from django.utils.safestring import mark_safe

admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(ProductSize)
admin.site.register(SubCategory)
admin.site.register(SubSubCategory)
admin.site.register(Company)


class GalleryInline(admin.TabularInline):
    fk_name = "product"
    model = Gallery


class ProductSizeInline(admin.TabularInline):
    fk_name = "product"
    model = ProductSize


@admin.register(ProductSite)
class ProductSiteAdmin(admin.ModelAdmin):
    inlines = [
        GalleryInline,
        ProductSizeInline,
    ]
    list_display = ("name", "price")
