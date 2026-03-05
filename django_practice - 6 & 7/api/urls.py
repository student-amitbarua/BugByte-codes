from django.urls import path
from .import views

urlpatterns = [
    path('products/', views.ProductLlistAPIView.as_view()),
    # path('products/', views.product_list),
    path('products/info/', views.product_info),
    path('products/<int:product_id>/', views.ProductDetailAPIView.as_view()),
    # path('products/<int:pk>/', views.product_Detail),
    path('orders/', views.OrderListAPIView.as_view()),
    path('user-orders/', views.UserOrderListAPIView.as_view()),

    # path('orders/', views.order_list)
]
