from django.urls import path

from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('toLatLong', views.toLatLong, name='toLatLong'),
    path('fromLatLong', views.fromLatLong, name='fromLatLong'),
    path('saveBLH', views.saveBLH, name='saveBLH'),
    path('saveXYZ', views.saveXYZ, name='saveXYZ'),
    path('displayAll', views.displayAll, name='displayAll')
]
