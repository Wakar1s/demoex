# hotel/views.py
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserRegistrationForm, OrderForm, ShiftAssignmentForm
from .models import User, Order, Shift

@login_required
def register_user(request):
    if request.user.role != 'manager':
        return redirect('home')
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'hotel/register_user.html', {'form': form})

@login_required
def dismiss_user(request, user_id):
    if request.user.role != 'manager':
        return redirect('home')
    user = get_object_or_404(User, id=user_id)
    user.status = 'dismissed'
    user.save()
    return redirect('register_user')

@login_required
def assign_shift(request):
    if request.user.role != 'manager':
        return redirect('home')
    if request.method == 'POST':
        form = ShiftAssignmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ShiftAssignmentForm()
    return render(request, 'hotel/assign_shift.html', {'form': form})

@login_required
def view_shifts(request):
    if request.user.role != 'manager':
        return redirect('home')
    shifts = Shift.objects.all()
    return render(request, 'hotel/view_shifts.html', {'shifts': shifts})

@login_required
def view_orders(request):
    if request.user.role not in ['manager', 'hotel_service']:
        return redirect('home')
    orders = Order.objects.all()
    return render(request, 'hotel/view_orders.html', {'orders': orders})

@login_required
def create_order(request):
    if request.user.role != 'room_service':
        return redirect('home')
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.created_by = request.user
            order.save()
            return redirect('home')
    else:
        form = OrderForm()
    return render(request, 'hotel/create_order.html', {'form': form})

@login_required
def change_order_status(request, order_id, status):
    order = get_object_or_404(Order, id=order_id)
    if request.user.role not in ['room_service', 'hotel_service']:
        return redirect('home')
    if (request.user.role == 'room_service' and status not in ['accepted', 'paid']) or (request.user.role == 'hotel_service' and status not in ['preparing', 'ready']):
        return redirect('home')
    order.status = status
    order.save()
    return redirect('view_orders')

@login_required
def home(request):
    return render(request, 'hotel/home.html')
