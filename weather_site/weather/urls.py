from django.urls import path
from .import views

urlpatterns = [
    path('', views.editor, name='editor'),
    path('delete_note/<int:noteid>/', views.delete_note, name='delete_note'),
    path('weather/weather-info.html', views.weather_info),
]