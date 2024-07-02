from django.contrib import admin

from app.models import Product, Category, Comment, Order

# Register your models here.
# admin.site.register(Category)
admin.site.register(Product)
# admin.site.register(Comment)
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    fields = ('title',)
    pass

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']