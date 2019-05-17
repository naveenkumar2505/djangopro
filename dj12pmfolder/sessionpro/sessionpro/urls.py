"""sessionpro URL Configuration

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
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from sessionapp import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^test_session/',views.test_session),
    url(r'^test_delete/',views.test_delete),
    url(r'^delete/',views.delete_session),
    url(r'^access/',views.access_session_data),
    url(r'^save/',views.save_session_data),

  ]
