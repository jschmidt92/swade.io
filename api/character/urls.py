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
    path("", get_all_characters, name="get_all_characters"),
    path("<int:id>/", get_character_by_id, name="get_character_by_id"),
    path("add/", add_money, name="add_money"),
    path("delete/<int:id>", delete_character, name="delete_character"),
    path("get/", get_character, name="get_character"),
    path("list/<int:discord_id>/", list_characters, name="list_characters"),
    path("money/", get_money, name="get_money"),
    path("new/", create_character, name="create_character"),
    path("remove/", remove_money, name="remove_money"),
]
