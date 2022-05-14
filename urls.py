from . import views
from django.urls import path
urlpatterns= [
    path('',views.primeload,name='primeload'),
    path('primelogic',views.primelogic,name='primelogic'),
    path('primeseries',views.primeseries,name='primeseries'),
    path('primeserieslogic',views.primeserieslogic,name='primeserieslogic'),

]