from django.urls import include, path

from booking import views

urlpatterns = [
    path('', views.Rooms.as_view(), name='main-view'),
]
