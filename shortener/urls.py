from django.urls import path

from shortener.views import index_view, redirect_view

urlpatterns = [
    path('', index_view, name='index'),
    path('redirect/', redirect_view)
]
