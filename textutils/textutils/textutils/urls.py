"""textutils URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
# added by ashvini padekar videos of 6 code
from .import views


#urlpatterns = [
 #   path('admin/', admin.site.urls),
  #  path('',views.index,name='index'),
   # path('about',views.about,name='about'),
    #path('navigator', views.navigator, name='navigator'),

#]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('analyze',views.analyze,name='analyze')
   # path('removepun',views.removepun,name='removepun'),
    #path('capitalizefirst', views.capitalizefirst, name='capitalizefirst'),
    #path('newlineremove', views.newlineremove, name='newlineremove'),
    #path('spaceremove', views.spaceremove, name='spaceremove'),
    #path('charcount', views.charcount, name='charcount'),
]
