from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout as auth_logout
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from allauth.socialaccount.models import SocialAccount
from users.forms import LoginForm, ProfileForm, PaymentForm

from users.models import UserProfile, Cottage, Booking
from django_daraja.mpesa.core import MpesaClient


def homepage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('welcome')  # Redirect to welcome page upon successful login
    else:
        # Create an empty dictionary for context information
        context = {}

        # If the username is available in session (e.g., after failed login attempt), pre-fill the field
        username = request.session.get('username')
        if username:
            context['username'] = username

        # Add any other relevant context information (e.g., error messages)

        return render(request, 'users/login.html', {'context': context})



def redirect_to_welcome(user):
    if SocialAccount.objects.filter(user=user, provider='google').exists():
        return redirect('welcome')  # Redirect to welcome page if authenticated via Google
    else:
        return redirect('home')  # Redirect to home page if authenticated via other means


def welcome_view(request):
    cottage = Cottage.objects.all()
    if request.user.is_authenticated:
        return render(request, 'users/home.html', { 'cottage': cottage})
    return redirect('users:home')  # Redirect to login page if not authenticated


def cart_items(request):
    cart_item = Booking.objects.filter(user=request.user)
    price = sum(item.cottage.cottage_price * item.stock for item in cart_item)
    return render(request, 'mycart.html', {'cart_item': cart_item, 'price': price})


def add_item(request, products_id):
    cottage = Cottage.objects.get(id=products_id)
    items, created = Booking.objects.get_or_create(cottage=cottage, user=request.user)
    items.stock += 1
    items.save()
    return redirect('users:cart')


def delete_item(request, item_id):
    items = Booking.objects.get(id=item_id)
    items.delete()
    return redirect('users:cart')





def payit(request, amount):
    mc = MpesaClient()
    phone_number = '0114340130'
    amount = int(amount)
    account_reference = 'reference'
    transaction_description = 'Pay_up'
    callback_url = 'https://api.darajambili.com/express-payment'
    print(mc.stk_push(phone_number, amount, account_reference, transaction_description, callback_url))
    return HttpResponse('Chill we processing stuff rn ')

def user_profile(request):
    profile = UserProfile.objects.all()
    return render(request, 'profile.html', {'profile': profile})


def user_details(request, pk):
    user_dets = UserProfile.objects.get(pk=pk)
    return render(request, 'profiled.html', {'user_dets': user_dets})


def edit_profile(request, pk):
    user_dets = get_object_or_404(UserProfile, pk=pk)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=user_dets)
        if form.is_valid():
            form.save()
            return redirect('user_profile')
    else:
        form = ProfileForm(instance=user_dets)
    return render(request, 'profile_edit.html', {'form': form})


def delete_profile(request, pk):
    user_dets = get_object_or_404(UserProfile, pk=pk)
    if request.method == 'POST':
        user_dets.delete()
        return redirect('user_profile')

def logout(request):
    auth_logout(request)
    return redirect('/')
