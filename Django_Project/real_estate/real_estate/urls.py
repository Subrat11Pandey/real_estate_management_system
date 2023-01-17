"""real_estate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from signup.views import signaction
from login.views import loginaction

admin.site.site_header = "SP Co. Admin"
admin.site.index_title = "Welcome to SP Coorporation"
admin.site.site_title = "SP Co."

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('signup.urls')),
    path('',include('login.urls')),

    
]
