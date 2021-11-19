# yomamabot/fb_yomamabot/urls.py
from django.conf.urls import include, url
from .views import BcbView
urlpatterns = [
    url(r'^9e235760e0505bfd5f5eca95b1956c65e44d415a4c880958d7/?$', BcbView.as_view()) 
        ]