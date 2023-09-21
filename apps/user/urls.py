from django.urls import path
#from .views import home_page

from . import views


urlpatterns = [
    path("users/", views.user_list, name="user-list"),
    path('login/', views.login_view, name="login-view"),
    path('profile/', views.profile, name="profile"),
]