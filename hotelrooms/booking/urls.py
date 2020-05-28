from django.urls import include, path

urlpatterns = [
    path('index/', views.index, name='main-view'),
]
