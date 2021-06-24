from django.urls import path
from .import views

urlpatterns = [
    path('', views.index),
    path('weather/weather-info.html', views.weather_info),
    path('weather/editor.html', views.editor, name='editor'),
    path('delete_note/<int:noteid>/', views.delete_note, name='delete_note'),
]