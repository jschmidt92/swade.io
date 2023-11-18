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
    path("", get_all_events, name="get_all_events"),
    path("<int:id>/", get_event_by_id, name="get_event_by_id"),
    path("attendance/", update_attendance, name="update_attendance"),
    path("attendance/get/", get_attendance, name="get_attendance"),
    path("delete/<int:id>/", delete_event, name="delete_event"),
    path("new/", create_event, name="create_event"),
]
