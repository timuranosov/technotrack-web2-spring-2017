"""application URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.decorators import login_required

from core.views import home
from .api import router

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('core.urls', namespace='core')),
    url(r'^social/', include('social_django.urls', namespace='social')),
    url(r'^api/', include(router.urls), name='rest_framework'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^$', login_required(home), name='home'),
    url(r'^search/', include('haystack.urls')),
]
