from django.urls import path     
from . import views
urlpatterns = [
    path('', views.desktop),
    path('login', views.index),	 
    path('dashboard', views.dashboard, name='autocomplete'),
    path('register', views.register),
    path('citation/<perpId>', views.citation),
    path('registeraction', views.registeraction),
    path('viewlog/<int:callId>', views.viewlog),
    path('loginaction', views.loginaction),
    path('logout', views.logout),
    path('addcall', views.addcall),
    path("submitcall", views.submitcall),
    path("clearcall/<int:callId>", views.clearcall),
    path("vcheck",views.vcheck, name='autocomplete'),
    path("status/<int:officerId>",views.status),
    path("changestatus/<officerId>", views.changestatus),
    path("criminalcitation", views.criminalcitation),
    path("logindispatch", views.logindispatch),
    path("dispatchlogin", views.dispatchlogin),
    path("dispatchdashboard", views.dispatchdashboard),
    path("dashboardvcheck", views.dashboardvcheck),
    path("10codesdispatch", views.tencodesdispatch),
    path("10codesleo", views.tencodesleo),
    path("editcall/<int:callId>", views.editcall),
    path("statusdispatch/<int:officerId>",views.statusdispatch),
    path("editstatusdispatch/<officerId>", views.editstatusdispatch),
    path("idcheck",views.idcheck, name="autocomplete1"),
    path("submitcitation", views.submitcitation),
    path("firedashboard", views.firedashboard),
    path("submitcallfire", views.submitcallfire),
    path("clearcallfire/<int:callId>", views.clearcallfire),
    path("addcallfire", views.addcallfire),
    path("changestatusfire/<int:officerId>", views.changestatusfire),
    path("firestatus<int:officerId>", views.firestatus)
    

]