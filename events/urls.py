from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("", views.events_home, name="events-home"),
    path("fest/<str:id>/", views.fest_events, name="fest-events"),
    path("test/", views.events_test, name="events-test"),
    path("register/<int:pk>", views.events_register, name="events-register"),
    path("unregister/<int:pk>", views.events_unregister, name="events-unregister"),
    path("event/<int:pk>/", views.single_event, name="single-event"),

]