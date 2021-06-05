 
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('books.urls')),
    # path('add/', include('music.urls'))
     path('admin/', admin.site.urls),
]