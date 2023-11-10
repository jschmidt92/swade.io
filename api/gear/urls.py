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
    path("", get_all_gear, name="get_all_gears"),
    path("<int:gear_id>/", get_gear, name="get_gear"),
    path("add/", add_gear, name="add_gear"),
    path("buy/", buy_gear, name="buy_gear"),
    path("delete/<int:gear_id>/", delete_gear, name="delete_gear"),
    path(
        "get/",
        get_gear_by_name,
        name="get_gear_by_name",
    ),
    path("new/", create_gear, name="create_gear"),
    path("remove/", remove_gear, name="remove_gear"),
    path("sell/", sell_gear, name="sell_gear"),
]
