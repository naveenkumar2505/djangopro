from django.conf.urls import url,include
from django.contrib import admin
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^books/',include('books.urls')),
    url(r'^movies/',include('movies.urls')),
    url(r'^games/',include('games.urls'))
]
