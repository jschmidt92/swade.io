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
    path("", get_all_powers, name="get_all_powers"),
    path("<int:power_id>/", get_power, name="get_power"),
    path("add/", add_power, name="add_power"),
    path("delete/<int:power_id>/", delete_power, name="delete_power"),
    path("new/", create_power, name="create_power"),
    path("remove/", remove_power, name="remove_power"),
]
