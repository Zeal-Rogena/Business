# forms.py
from django import forms

from users.models import UserProfile, Payment


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['user_name', 'user_bio', 'profile_pic']


class PaymentForm(forms.Form):
    class Meta:
        model = Payment
        fields = ['amount', 'phone_number']