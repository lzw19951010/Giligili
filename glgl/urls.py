"""glgl URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from glgl_app import views as glgl_app_views
from glgl_app import models as glgl_app_models
import glgl.settings as settings
urlpatterns = [
	url(r'^admin/', admin.site.urls),
	url(r'^$', glgl_app_views.index),
	url(r'^login/',glgl_app_models.login),
	url(r'^logout/',glgl_app_models.logout),
	url(r'^register/',glgl_app_models.register),
	url(r'^home/',glgl_app_views.home),
    url(r'^profile/',glgl_app_models.profile),
    url(r'^setpassword/',glgl_app_models.setPassword),
    url(r'^setpassword-suc/',glgl_app_views.setPasswordSuc),
    url(r'^upload/$', glgl_app_models.upload),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
]
