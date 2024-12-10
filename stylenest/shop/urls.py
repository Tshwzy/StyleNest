from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('cart/', views.cart, name='cart'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('add_to_cart/<int:pk>/', views.add_to_cart, name='add_to_cart'),
    path('checkout/', views.checkout, name='checkout'),
    # existing URLs
    path('staff/orders/', views.staff_order_list, name='staff_order_list'),
    path('staff/order/accept/<int:pk>/', views.accept_order, name='accept_order'),
    path('staff/order/prepare/<int:pk>/', views.prepare_order, name='prepare_order'),
    path('staff/order/deliver/<int:pk>/', views.deliver_order, name='deliver_order'),
    path('staff/order/cancel/<int:pk>/', views.cancel_order, name='cancel_order'),
    path('client/orders/', views.client_order_list, name='client_order_list'),
]
