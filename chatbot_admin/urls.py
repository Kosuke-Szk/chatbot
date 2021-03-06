"""chatbot_admin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from chatbot_admin import views
from chatbot_admin import apis, userapis

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^users$', views.show_users),
    url(r'^api/', include(apis.router.urls)),
    url(r'^userapi/', include(userapis.router.urls)),
    url(r'^usernames', views.show_usernames),
]
