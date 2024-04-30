from django.urls import path
from .views import home,about,services,ai,item,contact,search

urlpatterns = [
    
    path('',home,name='product-home'),
    path('about/',about,name='product-about'),
    path('services/',services,name='product-services'),
    path('ai/',ai,name='product-ai'),
    path('item/',item,name='product-item'),
    path('contact/',contact,name='product-contact'),
    path('search/',search, name='product-search'),
]
