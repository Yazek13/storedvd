from django.contrib import admin

from shop.models import Section, Product, Discount, Order, OrderLine, Gallery, Comment

admin.site.register(Section)
admin.site.register(Order)
admin.site.register(OrderLine)
admin.site.register(Gallery)
admin.site.register(Comment)


class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "section", "image", "price", "date")
    list_per_page = 10
    search_fields = ("title", "cast")


class DiscountAdmin(admin.ModelAdmin):
    list_display = ("code", "value_percent")


admin.site.register(Product, ProductAdmin)
admin.site.register(Discount, DiscountAdmin)