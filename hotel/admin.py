from django.contrib import admin
from .models import User, Order, Shift

admin.site.register(User)
admin.site.register(Order)
admin.site.register(Shift)