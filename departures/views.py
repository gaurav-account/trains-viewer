from django.http import Http404
from django.shortcuts import render
from departures.api_client.client import OcpAPIClient
from departures.api_client.client import StationNotFoundError
from django.http import HttpResponse
import json
import logging

# Get an instance of a logger
logger = logging.getLogger('django')

#This is the method to load data for home page. It renders the output in HTML.
#It fetches all station information.
def index(request):
    logger.info('Got a call from UI to get all stations, fetching required data ..')
    client = OcpAPIClient()
    all_stations = client.get_all_stations()
    context = {'all_stations': all_stations}
    return render(request, 'departures/index.html', context)

#API to load data for all stations. It returns the output in JSON format.
def indexapi(request):
    logger.info('Got a call from UI to get all stations, fetching required data ..')
    client = OcpAPIClient()
    all_stations = client.get_all_stations()
    context = {'all_stations': all_stations}
    data = json.dumps(all_stations)
    return HttpResponse(data, content_type='application/json')


#Method to fetch all the departures from the selected station. This renders the output in HTML format.
def departures(request, station_code):
    logger.info('Got a call from UI to get all departures, fetching required data ..')
    client = OcpAPIClient()
    try:
        departures = client.get_departures(station_code)
    except StationNotFoundError:
        raise Http404
    context = {'departures': departures, 'station_code': station_code}
    return render(request, 'departures/departures.html', context)

#API to fetch all the departures from the selected station. This returns the output in JSON format.
def departuresapi(request, station_code):
    logger.info('Got a call from UI to get all departures, fetching required data ..')
    client = OcpAPIClient()
    try:
        departures = client.get_departures(station_code)
    except StationNotFoundError:
        return HttpResponse('Station Not Found!!!', content_type='application/json',status=404)
    context = {'departures': departures, 'station_code': station_code}
    data = json.dumps(context)
    return HttpResponse(data, content_type='application/json')
