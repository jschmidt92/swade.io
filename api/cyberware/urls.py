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
    path("", get_all_cyberware, name="get_all_cyberware"),
    path("<int:cyberware_id>/", get_cyberware, name="get_cyberware"),
    path("add/", add_cyberware, name="add_cyberware"),
    path("buy/", buy_cyberware, name="buy_cyberware"),
    path("delete/<int:cyberware_id>/", delete_cyberware, name="delete_cyberware"),
    path(
        "get/",
        get_cyberware_by_name,
        name="get_cyberware_by_name",
    ),
    path("new/", create_cyberware, name="create_cyberware"),
    path("remove/", remove_cyberware, name="remove_cyberware"),
    path("sell/", sell_cyberware, name="sell_cyberware"),
]
