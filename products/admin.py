from django.contrib import admin
from.models import product, product_image ,product_review,category,brand

# Register your models here.


class product_image_admin(admin.TabularInline): # to add more images
    model = product_image




class product_admin(admin.ModelAdmin): 
    list_display=['name','flag','price']   # to display in admin panel
    inlines = [product_image_admin] # to add more imges




admin.site.register(product, product_admin)
admin.site.register(product_image)
admin.site.register(product_review)
admin.site.register(category)
admin.site.register(brand)
