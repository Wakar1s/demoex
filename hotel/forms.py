# hotel/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Order, Shift

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'role']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['details', 'status', 'payment_status', 'amount_clients', 'room_num']


class ShiftAssignmentForm(forms.ModelForm):
    class Meta:
        model = Shift
        fields = ['user', 'start_time', 'end_time']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user'].queryset = User.objects.filter(role__in=['room_service', 'hotel_service'], status='работает')


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'role', 'first_name', 'last_name', 'father_name', 'status']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['status'].initial = 'active'  # Default to active
