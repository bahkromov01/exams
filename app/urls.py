
from django.urls import path

from app.views import shop_index, products_list

urlpatterns = [
    path('shop_index/', shop_index, name='shop_index'),
    path('product_list/<int:product_id>', products_list, name='product_list')
]