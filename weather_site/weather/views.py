from django.shortcuts import redirect, render
import pandas as pd
import requests
from .models import Note

# Create your views here.

def index(request):
    return render(request, 'weather/index.html', {
    })

def weather_info(request):
    # read csv file with city names and latitudes and longitudes
    df = pd.read_csv('worldcities.csv')
    if 'city' in request.GET:
        city = request.GET['city'] 
        if df[df['city_ascii'] == city]['city_ascii'].any():

            lat = df[df['city_ascii'] == city]['lat'] 
            lon = df[df['city_ascii'] == city]['lng']

            url = "https://climacell-microweather-v1.p.rapidapi.com/weather/realtime"

            # query ClimaCell Weather API using latidude and longitude
            querystring = {"unit_system": "si",
            "fields": ["precipitation", "precipitation_type", "temp", "cloud_cover", "wind_speed",
            "weather_code"], "lat": lat, "lon": lon}

            # host and key found in ClimaCell Weather API Documentation
            headers = {
            'x-rapidapi-host': "climacell-microweather-v1.p.rapidapi.com",
            'x-rapidapi-key': "64606952fcmsh4e754c5afa969d3p101001jsn250893a3dd43"
            }

            response = requests.request("GET", url, headers=headers, params=querystring).json()

            # add response to a dictionary
            context = {'city_name': city,
            'temp': response['temp']['value'],
            'weather_code': response['weather_code']['value'],
            'wind_speed': response['wind_speed']['value'],
            'precipitation_type': response['precipitation_type']['value'] }
            return render(request, 'weather/weather-info.html', context)
        else:
            context = None
    else:
            context = None
            return render(request, 'weather/weather-info.html', context)

def editor(request):
    noteid = int(request.GET.get('noteid', 0))
    notes = Note.objects.all()

    if request.method == 'POST':
        noteid = int(request.POST.get('noteid', 0))
        title = request.POST.get('title')
        content = request.POST.get('content', '')

        if noteid > 0:
            note = Note.objects.get(pk=noteid)
            note.title = title
            note.content = content
            note.save()

            return redirect('/?noteid=%i' % noteid)
        else:
                note = Note.objects.create(title=title, content=content)

                return redirect('/?noteid=%i' % note.id)

    if noteid > 0:
        note = Note.objects.get(pk=noteid)
    else:
            note = ''

    context = {
        'noteid' : noteid,
        'notes' : notes,
        'note': note
    }

    return render(request, 'weather/editor.html', context)

def delete_note(request, noteid):
    note = Note.objects.get(pk=noteid)
    note.delete()

    return redirect('/?noteid=0')
