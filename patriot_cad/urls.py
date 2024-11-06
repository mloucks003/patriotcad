"""patriot_cad URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views( I)
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include     
from django.contrib import admin
from patriot_cadapp.models import User as U
from patriot_cadapp.models import Vehicle as V
from patriot_cadapp.models import Suspect as S
from patriot_cadapp.models import Call as C
from patriot_cadapp.models import Dispatcher as D
from patriot_cadapp.models import Fire as F
from patriot_cadapp.models import Citation as T
from patriot_cadapp.models import Arrest as A

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('patriot_cadapp.urls'))
]

admin.site.site_header = 'Wicked RP Admin Panel'

