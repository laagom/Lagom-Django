from django.urls import path

from shortener.views import get_user, index_view, redirect_view, register

urlpatterns = [
    path('', index_view, name='index'),
    path('redirect/', redirect_view),
    path('user/<int:user_id>', get_user),

    # REGISTER
    path('register', register, name='register'),
]
