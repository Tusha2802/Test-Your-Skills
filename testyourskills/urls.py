"""testyourskills URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from tys import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('a/',views.a),
    path('index/',views.index),
    path('b/',views.cs),
    path('c/',views.maths),
    path('d/',views.gk),
    path('b1/',views.cstest),
    path('removeall/',views.removeall),
    path('remove/<int:stdid>',views.remove,name="rem"),
    path('update/<int:stdid>',views.update,name="upd"),
    path('login/',views.indexuser),
    path('a2/',views.a1),
    path('resulthistory/',views.history),
    path('',views.homepagemenu),
    path('manageuser/',views.manageuser),
    path('about_us/',views.aboutus),
    path('contact_us/',views.contactus),
]
