from django.urls import path, reverse_lazy
from hotel.views import register_user, dismiss_user, assign_shift, view_orders, create_order, change_order_status, home, view_shifts
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import AuthenticationForm
urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', register_user, name='register_user'),
    path('dismiss/<int:user_id>/', dismiss_user, name='dismiss_user'),
    path('assign_shift/', assign_shift, name='assign_shift'),
    path('view_shifts/', view_shifts, name='view_shifts'),
    path('orders/', view_orders, name='view_orders'),
    path('orders/create/', create_order, name='create_order'),
    path('orders/<int:order_id>/status/<str:status>/', change_order_status, name='change_order_status'),
    path('', home, name='home'),
    path('logout/', auth_views.LogoutView.as_view(
        next_page=reverse_lazy('login') # Assuming 'login' is the name of your login URL
    ), name='logout'),
    path('login/', auth_views.LoginView.as_view(authentication_form=AuthenticationForm, redirect_authenticated_user=True), name='login'),
]
