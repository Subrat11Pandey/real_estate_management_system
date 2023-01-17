

from django.contrib import admin
from django.urls import path
from login import views
# from signup import views


urlpatterns = [
    path("home/",views.home, name="home"),
    path("login/",views.loginaction, name="loginaction"),
    path("contact/",views.contactus, name="contactus"),
    path("sell/",views.sellprops, name="sellprop"),
    path("allprops/",views.allprops, name="allprops"),
    path("if/",views.showif, name="showif"),
    path("villa/",views.showvilla, name="showvilla"),
    path("bf/",views.showbf, name="showbf"),
    path("apart/",views.showappartment, name="showappartment"),
    path("bought/",views.buyprops, name="buyprop"),
    path("sort/",views.sort, name="sort"),
    path("adminlpage/",views.adminp, name="adminp"),
    path("adminpage/",views.alogin, name="admin"),
    path("dashboard/",views.alogin, name="admin"),
    path("asset/",views.asset, name="asset"),
    path("buyersallprop/",views.buyersallprop, name="buyersallprop"),
    path("mesfilter/",views.mesfilter, name="mesfilter"),
    path("data/",views.data, name="data"),
    path("about/",views.about, name="about"),


]