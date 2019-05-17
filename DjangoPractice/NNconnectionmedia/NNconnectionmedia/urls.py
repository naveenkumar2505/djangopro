from django.conf.urls import url
from django.contrib import admin
from NNconnectionapp import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/',views.home),
    url(r'^reg/',views.reg),
    url(r'^login/',views.login)
]
