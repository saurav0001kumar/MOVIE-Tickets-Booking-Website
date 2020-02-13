"""movieticket URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from movieapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('upcoming/',views.upcoming),
    path('index/upcoming/',views.upcoming),
    path('login/',views.login),
    path('signup/',views.signup),
    path('booked/',views.booked),
    path('index/',views.index),
    path('about/',views.about),
    path('index/about/',views.about),
    path('details/<int:id>/',views.details),
    path('index/details/<int:id>/',views.details),
    path('updetails/<int:id>/',views.updetails),
    path('index/updetails/<int:id>/',views.updetails),
    path('aboutmore/',views.aboutmore)
]
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
