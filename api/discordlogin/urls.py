"""
URL configuration for swadeBotIO project.

The `urlpatterns` list routes URLs to views. For more information please see:
https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
1. Add an import:  from my_app import views
2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
1. Add an import:  from other_app.views import Home
2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
1. Import the include() function: from django.urls import include, path
2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import *

urlpatterns = [
    path("<str:discord_id>/", get_user_by_id, name="get_user"),
    path("auth/user/", get_authenticated_user, name="get_authenticated_user"),
    path("oauth2/login/", discord_login, name="oauth2_login"),
    path(
        "oauth2/login/redirect/",
        discord_login_redirect,
        name="discord_login_redirect",
    ),
]
