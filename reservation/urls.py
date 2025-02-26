from django.contrib import admin 
from django.urls import path 
from . import views 
from rest_framework.authtoken.views import obtain_auth_token  

urlpatterns = [ 
    path('sayHello/', views.sayHello, name='sayHello'), 
    path('', views.index, name='index'),
    path('menu/', views.MenuItemsView.as_view(), name='menu-list'),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    path('api-token-auth/', obtain_auth_token),
]