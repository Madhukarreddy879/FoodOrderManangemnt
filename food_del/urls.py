from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views

from orders.api.views import (ApiHomepage , OrderListAPIView, OrderDetailAPIView,
OrderItemListAPIView, OrderItemDetailAPIView,) 


from products.api.views import ProductListAPIView, ProductDetailAPIView, CategoryListApiView,ProductListApiAuthView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('auth/', views.obtain_auth_token,),

    path('api/order-list/', OrderListAPIView.as_view(), name='order_list'),
    path('api/order-detail/<int:pk>/', OrderDetailAPIView.as_view(), name='order_detail'),
    path('api/order-item-list', OrderItemListAPIView.as_view(), name='order_item_list'),
    path('api/order-item-detail/<int:pk>/', OrderItemDetailAPIView.as_view(), name='order_item_detail'),   
    


    path('api/product-list/', ProductListAPIView.as_view(), name='product_list'),
    path('api/product-detail/<int:pk>/', ProductDetailAPIView.as_view(), name='product_detail'),
    path('api/category-list/', CategoryListApiView.as_view(), name='category_list'),
    path('api/auth/products/', ProductListApiAuthView.as_view(), name='product_auth_view'),
    path('api/', ApiHomepage), 
]

