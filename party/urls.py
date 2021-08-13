from django.contrib import admin
from django.urls import path,include
from dip import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home-page'),
    path('dip/',include('dip.urls')),
    #path('accounts/',include('django.contrib.auth.urls')),
]
