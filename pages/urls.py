from django.urls import path
from . import views
from .views import (
    HomeView,
    productDetailView,
    add_to_cart,
    orderSumaryView
)
from django.conf.urls.static import static
from django.conf import settings

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('search/', views.search, name='search'),
    path('product/<slug:slug>/', productDetailView.as_view(), name='product'),
    path('add-to-cart/<slug:slug>/', add_to_cart, name='add-to-cart'),
    path('save/', orderSumaryView.as_view(), name='save'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)