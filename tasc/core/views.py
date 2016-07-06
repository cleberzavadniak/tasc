import json

from django.shortcuts import render  # , redirect
from django.http import HttpResponse
from widgets import widgets
# from django.template.loader import render_to_string
# from django.contrib import messages


def index(r):
    return render(r, 'index.html', {
        'page_title': 'TASC',
    })


def cells(r):
    counter = int(r.GET.get('counter', 0))
    time_lapse = int(r.GET.get('time_lapse', None))

    messages = []
    for coordinates, function in widgets.items():
        content = function(r, coordinates, counter, time_lapse)

        if content is not None:
            messages.append({
                'coordinates': coordinates,
                'content': content
            })

    data = json.dumps({
        'messages': messages
    })
    return HttpResponse(data, content_type='application/json')
