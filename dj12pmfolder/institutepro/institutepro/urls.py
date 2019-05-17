from django.conf.urls import url
from django.contrib import admin
from instituteapp import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.home)
]
