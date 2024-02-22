from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout, authenticate, login
from allauth.socialaccount.models import SocialAccount
from .forms import LoginForm  # Import your login form

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from allauth.socialaccount.models import SocialAccount

from .models import Products, Items


def homepage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('welcome')  # Redirect to welcome page upon successful login
    return render(request, 'users/login.html')


def redirect_to_welcome(user):
    if SocialAccount.objects.filter(user=user, provider='google').exists():
        return redirect('welcome')  # Redirect to welcome page if authenticated via Google
    else:
        return redirect('home')  # Redirect to home page if authenticated via other means


def welcome_view(request):
    produce = Products.objects.all()
    if request.user.is_authenticated:
        return render(request, 'users/after.html', {'user': request.user, 'produce': produce})
    return redirect('home')  # Redirect to login page if not authenticated


def cart_items(request):
    cart_item = Items.objects.filter(user=request.user)
    price = sum(item.product * item.quantity for item in cart_item)
    return render(request, 'mycart.html', {'cart_item': cart_item, })


def add_item(request, products_id):
    product = Products.objects.get(id=products_id)
    items, create = Items.objects.get_or_create(product=product, user=request.user)
    items.stock = +1
    items.save()
    return redirect('cart:cart_items')


def delete_item(request, item_id):
    items = Items.objects.get(id=item_id)
    items.delete()
    return redirect('cart:cart_items')


def logout(request):
    auth_logout(request)
    return redirect('/')
