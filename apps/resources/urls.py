from django.urls import path
#from .views import home_page
from . import views




urlpatterns = [
    path('', views.home_page, name= 'home-page'),
    path("resources/<int:id>", views.resource_detail, name="resources-detail"),
    path('resources/post/', views.resource_post, name='resource-post')
]