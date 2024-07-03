
from django.urls import path

from app.views.home import about_page
from app.views.views import shop_index, products_detail, category_index, add_comment, add_order

urlpatterns = [
    path('shop_index/', shop_index, name='shop_index'),
    path('category/<slug:category_slug>/products', category_index, name='category_index'),
    path('products_detail/<slug:product_slug>', products_detail, name='products_detail'),
    path('about_page/', about_page, name='about_page'),

    # comment path
    path('product/<slug:product_slug>/detail/add-comment/', add_comment, name='add_comment'),
    path('product/<slug:product_slug>/detail/add-order/', add_order, name='add_order'),
]