from django.contrib.auth.views import PasswordResetCompleteView, PasswordResetConfirmView, PasswordResetDoneView, \
    PasswordResetView
from django.urls import path
from . import views
from .views import confirmation_view, send_email

urlpatterns = [
    path('', views.index, name = 'index'),
    path('detail', views.detail, name = 'detail'),
    path('category', views.category, name = 'category'),
    path('register', views.register, name = 'register'),
    path('login', views.login, name = 'login'),
    path('logout', views.logout, name = 'logout'),
    path('account', views.account, name = 'account'),
    path('product', views.product, name = 'product'),
    path('addProduct', views.addProduct, name = 'addProduct'),
    path('deleteProduct', views.deleteProduct, name = 'deleteProduct'),
    path('editProduct', views.editProduct, name = 'editProduct'),
    path('cart', views.cart, name = 'cart'),
    path('chooseSize', views.chooseSize, name = 'chooseSize'),
    path('addToCart', views.addToCart, name = 'addToCart'),
    path('profile', views.profile, name = 'profile'),
    path('deleteFromCart', views.deleteFromCart, name = 'deleteFromCart'),
    path('yourOrder', views.yourOrder, name = 'yourOrder'),
    path('hiddenOrder', views.hiddenOrder, name = 'hiddenOrder'),
    path('hiddenOrder1', views.hiddenOrder1, name = 'hiddenOrder1'),
    path('cancelOrder', views.cancelOrder, name = 'cancelOrder'),
    path('completeOrder', views.completeOrder, name = 'completeOrder'),
    path('customerOrder', views.customerOrder, name = 'customerOrder'),
    path('registerSeller', views.registerSeller, name = 'registerSeller'),
    path('myshop', views.myshop, name = 'myshop'),
    path('categoryShop', views.categoryShop, name = 'categoryShop'),
    path('detailShop', views.detailShop, name = 'detailShop'),
    path('deleteAccount', views.deleteAccount, name = 'deleteAccount'),
    path('registerAdmin', views.registerAdmin, name = 'registerAdmin'),
    path('search', views.search, name = 'search'),
    path('searchShop', views.searchShop, name = 'searchShop'),
    path('increase', views.increase, name = 'increase'),
    path('decrease', views.decrease, name = 'decrease'),
    path('password-reset/', PasswordResetView.as_view(template_name='password_reset.html'),name='password-reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(template_name='password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),name='password_reset_confirm'),
    path('password-reset-complete/', PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
    path('confirmation/<str:token>/', confirmation_view, name='confirmation'),
    path('confirmation-is-seller', send_email, name='send_email'),
    path('addProduct', views.addProduct, name='addProduct')
]