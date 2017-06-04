from django.conf.urls import url
from api import views

urlpatterns = [
    url(r'^gamerooms/$', views.get_or_create_game_room),
]
