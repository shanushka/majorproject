"""avail URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from .models import MyMobileModel
from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/',include('accounts.url'),name='register'),
    url(r'^$', views.home,name="home"),
    url(r'^about/',views.about,name="about"),
    url(r'^signin/', views.signin, name="signin"),
    url(r'^categories/', views.categories, name="categories"),
    url(r'^compare/', views.compare, name="compare"),
    url(r'^mobiledetails/',views.mobileDetails,name="mobiledetails"),
    url(r'^mobiles/', views.mobiles, name="mobiles",),
    url(r'^accessories/',views.Accesories,name="accessories"),
    url(r'^others/', views.Others, name="others"),
    url(r'^samsung/', views.samsung, name="samsung"),
    url(r'^customresponse/', views.custom_response, name="custom_response")

]
