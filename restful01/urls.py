"""
Book: Django RESTful Web Services
Author: Gaston C. Hillar - Twitter.com/gastonhillar
Publisher: Packt Publishing Ltd. - http://www.packtpub.com
"""
"""restful01 URL Configuration

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
from django.urls import path, include, re_path
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from rest_framework import urls
from rest_framework_simplejwt import views as jwt_views


urlpatterns = [
    #path("", include("toys.urls")),
    re_path(r'^admin/', admin.site.urls),
    #re_path(r'^', include('drones.urls')),
    re_path(r'^wprod/', include('wprod.urls')),
    #re_path(r'^api-auth/', include('rest_framework.urls')),
    path('login/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh-token/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('token-verify',jwt_views.TokenVerifyView.as_view(), name='token-verify'),
]
