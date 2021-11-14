from django.contrib import admin

from shop.models import Section, Product, Discount, Order, OrderLine, Gallery, Comment

admin.site.register(Section)
admin.site.register(Product)
admin.site.register(Discount)
admin.site.register(Order)
admin.site.register(OrderLine)
admin.site.register(Gallery)
admin.site.register(Comment)
