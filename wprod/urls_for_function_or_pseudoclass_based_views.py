from django.urls import path, re_path
from wprod import views


urlpatterns = [
    re_path(r'^bls/$', views.bl_list),
    re_path(r'^bls/(?P<pk>[0-9]+)$', views.bl_detail),
    re_path(r'^blis/$', views.bli_list),
    re_path(r'^blis/(?P<pk>[0-9]+)$', views.bli_detail),
]
