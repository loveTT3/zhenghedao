from django.conf.urls import url
from django.contrib import admin
from app1 import views as app1_views, urls as app1_app1
# from app1 import views as app1_views, urls as app1_app1


urlpatterns = [
    url(r'^$', app1_views.app1base),
    # url(r'^base/', app1_views.base),

]
