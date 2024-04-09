from django.urls import path, include
from .views import *
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('not-found/', not_found, name='not_found'),
    path('cart/', cart, name='cart'),
    path('checkout/', checkout, name='checkout'),
    path('contact/', contact, name='contact'),
    path('home/', home_2, name='home_2'),
    path('news/', news, name='news'),
    path('shop/', shop, name='shop'),
    path('product/<int:product_id>/', single_product, name='single_product'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('register/', register, name='register'),
    path('s_news/', single_news, name='single_news'),
    path('s_product/', single_product, name='single_product'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]