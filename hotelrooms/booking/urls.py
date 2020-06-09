from django.urls import path

from booking import views

urlpatterns = [
    path('', views.Rooms.as_view(), name='main-view'),
    path('room/book/<int:pk>', name="book", view=views.BookRoom.as_view()),
    path('room/view/<int:pk>', name="room", view=views.RoomDetail.as_view()),
    path('room/create', name="create_room", view=views.CreateRoomView.as_view()),
    path('room/edit/<int:pk>', name="edit_room", view=views.EditRoomView.as_view()),
]
