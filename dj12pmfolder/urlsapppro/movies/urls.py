from django.conf.urls import url
from movies import views
urlpatterns = [
    url(r'^horror/', views.horror),
    url(r'^worrior/', views.warrior),
]