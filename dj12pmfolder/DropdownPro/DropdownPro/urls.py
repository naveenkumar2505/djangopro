from django.conf.urls import url
from django.contrib import admin
from dropdownapp import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^drop/',views.dropview)
]
