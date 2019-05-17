from django.conf.urls import url
from django.contrib import admin
from httpapp import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^insert/',views.inserting),
    url(r'^search/',views.search),
    url(r'^update/',views.update),
    url(r'^display/',views.display),
    url(r'^delete/',views.delete),
    url(r'^login/',views.login)
]
