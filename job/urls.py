from . import views
from django.urls import path


urlpatterns = [

    path('', views.portal, name='portal'),
    path('apply', views.apply, name='apply'),
    # path('query',views.query,name='query'),
]