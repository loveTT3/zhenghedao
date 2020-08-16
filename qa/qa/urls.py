"""qa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from app1 import views as app1_views, urls as app1_app1
# from app1 import views as app1_views, urls as app1_app1


urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^login/', app1_views.login),
    url(r'^base/', app1_views.base),
    # url(r'^login/', app1_views.login),

    # 路由分发到app01和app02的urls文件中
    url(r'^app1/',include('app1.urls')),
    # url(r'^app02/',include('app02.urls')),
]
