from django.urls import path

from shortener.views import get_user, index_view, login_view, logout_view, redirect_view, register_view

urlpatterns = [
    path('redirect/', redirect_view),
    path('user/<int:user_id>', get_user),

    # INDEX
    path('', index_view, name='index'),

    # REGISTER
    path('register', register_view, name='register'),

    # LOGIN, LOGOUT
    path('login', login_view, name='login'),
    path('logout', logout_view, name='logout'),
]
