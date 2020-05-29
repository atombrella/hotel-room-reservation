from django.urls import include, path

from booking import views

urlpatterns = [
    path('index/', views.Rooms, name='main-view'),
]
