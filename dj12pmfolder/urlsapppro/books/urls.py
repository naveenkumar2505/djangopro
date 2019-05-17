from django.conf.urls import url
from books import views
urlpatterns = [
    url(r'^bb1/',views.bb1),
    url(r'^bb2/',views.bb2)
]