from django.contrib import admin
from django.urls import path , include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , include('main.urls') , name="imp"),
    path('main/' ,  TemplateView.as_view(template_name = 'main/main.html') , name='main'),
    path('user/' , include('hern_a.urls'), name="user"),
   
]
