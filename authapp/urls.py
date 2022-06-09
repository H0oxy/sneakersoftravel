from django.urls import path

# from .views import BaseView, ProductDetailView, CategoryDetailView, CartView, AddToCartView, DeleteFromCartView, ChangeQTYView, ChangeSizeView, CheckoutView, MakeOrderView
import authapp.views as authapp
app_name = 'authapp'

urlpatterns = [
    path('login/', authapp.login, name='login'),
    path('register/', authapp.register, name='register'),
    path('logout/', authapp.logout, name='logout'),

]

