from django.urls import path

from shortener.views import get_user, index_view, redirect_view

urlpatterns = [
    path('', index_view, name='index'),
    path('redirect/', redirect_view),
    path('get_user/<int:user_id>', get_user),
]
