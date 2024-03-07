from django.urls import path
from users import views

app_name = 'users'

urlpatterns = [
    path("", views.homepage, name='home'),  # URL for the home page
    path("welcome/", views.welcome_view, name='welcome'),  # URL for the welcome page
    path("logout/", views.logout, name='logout'),  # URL for logout
    path("cart/", views.cart_items, name='cart'),  # URL for carts
    path("add/<int:products_id>/", views.add_item, name='add'),  # URL for adding stuff
    path('payit/<int:amount>/', views.payit, name='payit')
]
