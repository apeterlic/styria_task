from django.shortcuts import render
from .models import Attacks
import requests
import datetime
from datetime import datetime
from datetime import timedelta
from django.db.models import Q


def show(request):
    response = Attacks.objects.all()
    end_date = datetime.now().date()

    if 'dateStart' in request.GET:
        start_date = request.GET['dateStart']

        if 'dateEnd' in request.GET:
            end_date = request.GET['dateEnd']

        response = response.filter(date__date__range=(start_date, end_date))

    else:
        response = response.filter(date__gte=datetime.now() - timedelta(30 * 3))

    if 'country' in request.GET:
        c = request.GET['country']
        response = response.filter(country__contains=c)

    if 'location' in request.GET:
        l = request.GET['location']
        response = response.filter(location__contains=l)

    if 'town' in request.GET:
        town = request.GET['town']
        response = response.filter(town__contains=town)

    map_points = response

    return render(request, "maps/maps.html", {
        'map_points': map_points,
        'key': 'AIzaSyAhCw0SCeb5bTNGQo_UHK8C2aHb6IKBJa8'
    })


def search(request):
    search_result = {}
    output_line = []

    if 'text' in request.GET:
        text = request.GET['text']
        response = Attacks.objects.filter(Q(narrative__contains=text))

        for record in response:
            new_record = record.narrative.replace(text, "<span>" + text + "</span>")
            output_line.append(new_record)

        search_result = response

    return render(request, 'maps/search.html', {'search_result': search_result, 'output_line': output_line})


def home(request):
    Attacks.objects.all().delete()
    response = requests.get('https://api.dronestre.am/data')
    data = response.json()

    for d in data['strike']:
        Attacks.objects.create(
            idNo=d['_id'],
            articles=d['articles'],
            bij_link=d['bij_link'],
            bij_summary_short=d['bij_summary_short'],
            bureau_id=d['bureau_id'],
            children=d['children'],
            civilians=d['civilians'],
            country=d['country'],
            date=d['date'],
            deaths=d['deaths'],
            deaths_max=d['deaths_max'],
            deaths_min=d['deaths_min'],
            injuries=d['injuries'],
            lat=d['lat'],
            location=d['location'],
            lon=d['lon'],
            names=d['names'],
            narrative=d['narrative'],
            number_field = d['number'],
            target=d['target'],
            town = d['town'],
            tweet_id = d['tweet_id'],
        )
    return render(request, "maps/maps.html", {
        'data': data['strike'],
        'key': 'AIzaSyAhCw0SCeb5bTNGQo_UHK8C2aHb6IKBJa8'
    })

