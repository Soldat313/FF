from django.urls import path , include
from .views import Register

urlpatterns = [
    path('',  include('django.contrib.auth.urls')),
    path('registration/' , Register.as_view() , name="register"),
]
