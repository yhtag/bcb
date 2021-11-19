# bcb/bcb/urls.py
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^fb_bcb/', include('fb_bcb.urls')),
]

#localhost:8000/fb_bcb/
