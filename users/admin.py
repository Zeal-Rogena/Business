from django.contrib import admin

from users.models import Cottage, Booking, UserProfile

# Register your models here.
admin.site.register(Cottage)
admin.site.register(Booking)
admin.site.register(UserProfile)
