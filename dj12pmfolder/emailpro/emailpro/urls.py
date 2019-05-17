from django.conf.urls import url
from django.contrib import admin
from emailapp import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^mail/',views.mail)
]
