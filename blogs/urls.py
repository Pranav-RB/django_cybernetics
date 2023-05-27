from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="blogs-index"),
    path("about/",views.about, name="blogs-about"),
    path("gallery/",views.gallery, name="blogs-gallery"),
    path("fests/",views.fests, name="blogs-fests"),
    path("fest/<str:id>/",views.fest, name="fests-event"),
    path("com-mem/",views.com_mem, name="com-mem"),
]