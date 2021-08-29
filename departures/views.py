from django.http import Http404
from django.shortcuts import render

from departures.api_client.client import OcpAPIClient
from departures.api_client.client import StationNotFoundError
from django.http import HttpResponse
import json
import logging

# Get an instance of a logger
logger = logging.getLogger('django')

#This is the method to load data for home page.
#It fetches all station information.
def index(request):
    logger.info('Got a call from UI to get all stations, fetching required data ..')
    client = OcpAPIClient()
    all_stations = client.get_all_stations()
    context = {'all_stations': all_stations}
    #Uncomment below lines if we need json in response of API
    #data = json.dumps(all_stations)
    #print(data)
    #return HttpResponse(data, content_type='application/json')
    return render(request, 'departures/index.html', context)

#Method to fetch all the departures from the selected station.
def departures(request, station_code):
    logger.info('Got a call from UI to get all departures, fetching required data ..')
    client = OcpAPIClient()
    try:
        departures = client.get_departures(station_code)
    except StationNotFoundError:
        raise Http404
    context = {'departures': departures, 'station_code': station_code}
    # Uncomment below lines if we need json in response of API
    #data = json.dumps(context)
    # print(data)
    #return HttpResponse(data, content_type='application/json')
    return render(request, 'departures/departures.html', context)
