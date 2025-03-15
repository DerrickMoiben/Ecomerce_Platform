from . import views
from django.urls import path
urlpatterns = [
    path('owner_singup/', views.owner_singup),
    path('owner_login/', views.owner_login),
    path('owner_logout/', views.owner_logout),
]