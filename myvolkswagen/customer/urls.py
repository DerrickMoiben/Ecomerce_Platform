
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('landingpage/', views.landingpage, name='landingpage'),
    path('display_products/', views.display_products, name='display_products'),
    path('product_details/<int:product_id>/', views.product_details, name='product_details'),
    path('product_payment/<int:product_id>/', views.product_payment, name='product_payment'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)