from django.urls import path
from . import views
''' This is the tab search in shop  app '''
urlpatterns = [
    path('', views.index, name = 'shopingHome'),
    path('about/', views.about, name='About Us'),
    path('contact', views.contact, name='Contact Us'),
    path('tracker', views.tracker, name='Tracker'),
    path('search', views.search, name='Search'),
    path('checkout', views.checkout, name='CheckOut'),
    path('productView/<int:prid>', views.productview, name='Product View'),
    path('product/', views.productlist, name='Productitems'),


]
