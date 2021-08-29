from django.http import Http404
from django.shortcuts import render

from departures.api_client.client import OcpAPIClient
from departures.api_client.client import StationNotFoundError
import logging

# Get an instance of a logger
logger = logging.getLogger('django')

def index(request):
    logger.info('Got a call from UI to get all stations, fetching required data ..')
    client = OcpAPIClient()
    all_stations = client.get_all_stations()
    context = {'all_stations': all_stations}
    return render(request, 'departures/index.html', context)

def departures(request, station_code):
    logger.info('Got a call from UI to get all departures, fetching required data ..')
    client = OcpAPIClient()
    try:
        departures = client.get_departures(station_code)
    except StationNotFoundError:
        raise Http404
    context = {'departures': departures, 'station_code': station_code}
    return render(request, 'departures/departures.html', context)
