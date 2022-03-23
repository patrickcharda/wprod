from django.urls import re_path
from wprod import views


urlpatterns = [
    re_path(r'^bls/$', views.BL_EnteteList.as_view(), name=views.BL_EnteteList.name),
    re_path(r'^bls/(?P<pk>[0-9]+)$', views.BL_EnteteDetail.as_view(), name=views.BL_EnteteDetail.name),
    re_path(r'^blis/$', views.BL_LigneList.as_view(), name=views.BL_LigneList.name),
    re_path(r'^blis/(?P<pk>[0-9]+)$', views.BL_LigneDetail.as_view(), name=views.BL_LigneDetail.name),
    re_path(r'^$', views.ApiRoot.as_view(), name=views.ApiRoot.name),
]
