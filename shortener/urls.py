from django.urls import path

from shortener.views import (
    redirect_view,
    get_user,
    index_view,
    payplan_list_view,
    url_list,
    user_list_view,
    login_view,
    logout_view,
    register_view,
)

urlpatterns = [
    path("redirect/", redirect_view),
    path("user/<int:user_id>", get_user),
    # INDEX
    path("", index_view, name="index"),
    # REGISTER
    path("register", register_view, name="register"),
    # LOGIN, LOGOUT
    path("login", login_view, name="login"),
    path("logout", logout_view, name="logout"),
    # LIST
    path("payplan/list", payplan_list_view, name="playplan_list"),
    path("user/list", user_list_view, name="user_list"),
    path("url_list", url_list, name="url_list"),
]
