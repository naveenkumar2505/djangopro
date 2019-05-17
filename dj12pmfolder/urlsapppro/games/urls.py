from django.conf.urls import url
from games import views
urlpatterns = [
    url(r'^cricket/',views.cricket ),
    url(r'^hockey/',views.hockey ),
]