from django.urls import path
from users import views

urlpatterns = [
    path("", views.homepage, name='home'),  # URL for the home page
    path("welcome/", views.welcome_view, name='welcome'),  # URL for the welcome page
    path("logout/", views.logout, name='logout'),  # URL for logout

]