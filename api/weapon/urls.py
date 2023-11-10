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
    path("", get_all_weapons, name="get_all_weapons"),
    path("<int:weapon_id>/", get_weapon, name="get_weapon"),
    path("add/", add_weapon, name="add_weapon"),
    path("buy/", buy_weapon, name="buy_weapon"),
    path("delete/<int:weapon_id>/", delete_weapon, name="delete_weapon"),
    path(
        "get/",
        get_weapon_by_name,
        name="get_weapon_by_name",
    ),
    path("new/", create_weapon, name="create_weapon"),
    path("remove/", remove_weapon, name="remove_weapon"),
    path("sell/", sell_weapon, name="sell_weapon"),
]
