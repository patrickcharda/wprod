"""
Book: Django RESTful Web Services
Author: Gaston C. Hillar - Twitter.com/gastonhillar
Publisher: Packt Publishing Ltd. - http://www.packtpub.com
"""
from django.urls import path, re_path
from toys import views

urlpatterns = [
	path('toys/', views.toy_list),
	re_path(r'^toys/(?P<pk>[0-9]+)$', views.toy_detail),
]