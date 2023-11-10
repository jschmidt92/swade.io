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
    path("", get_all_encounters, name="get_all_encounters"),
    path("<int:encounter_id>/", get_encounter, name="get_encounter"),
    path("add/character/", add_character, name="add_character"),
    path("add/npc/", add_npc, name="add_npc"),
    path(
        "<int:encounter_id>/characters/",
        get_characters,
        name="get_characters",
    ),
    path("<int:encounter_id>/npcs/", get_npcs, name="get_npcs"),
    path("new/", create_encounter, name="create_encounter"),
    path(
        "delete/<int:encounter_id>/",
        delete_encounter,
        name="delete_encounter",
    ),
    path("remove/character/", remove_character, name="remove_character"),
    path("remove/npc/", remove_npc, name="remove_npc"),
]
