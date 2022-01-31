from django.urls import path
from order.views import order_view

urlpatterns = [
    path('', order_view)
]
