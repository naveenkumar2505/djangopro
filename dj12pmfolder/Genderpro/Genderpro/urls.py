from django.conf.urls import url
from django.contrib import admin
from Genderapp import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.home),
    url(r'^girls',views.girls),
    url(r'^boys',views.boys),
]
