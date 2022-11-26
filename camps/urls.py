from django.urls import path
from . import views



urlpatterns = [
    path('livebloodcamps/', views.livebloodcamps, name="livebloodcamps")
]