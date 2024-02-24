from django.urls import path
from django.contrib import admin

from products.views import ProductViewSet

urlpatterns = [
    path('products', ProductViewSet.as_view({
        'get': 'list',
        'post': 'create',
    })),
    path('products/<str:pk>', ProductViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy',
    })),
]
