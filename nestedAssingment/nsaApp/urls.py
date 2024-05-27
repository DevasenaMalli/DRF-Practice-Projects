from django.urls import path
from nsaApp import views

urlpatterns = [
    path('order/',views.OrderListView.as_view()),
    path('order/<int:pk>',views.OrderDetailsView.as_view()),
    path('customer/',views.CustomerListView.as_view()),
    path('customer/<int:pk>',views.CustomerDetailsView.as_view()),
    
    
]
