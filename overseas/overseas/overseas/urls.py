from django.contrib import admin
from django.urls import path,include
from overseasApp import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('overseasApp.urls')),
]
