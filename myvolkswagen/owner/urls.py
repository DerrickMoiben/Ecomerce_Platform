from . import views
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('owner_singup/', views.owner_singup, name='owner_singup'),
    path('owner_login/', views.owner_login, name='owner_login'),
    path('owner_logout/', views.owner_logout, name='owner_logout'),
    path('owner_dashboard/', views.owner_dashboard, name='owner_dashboard'),
    path('add_products/', views.add_products, name='add_products'),
    path('all_products/', views.all_products, name='all_products'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)