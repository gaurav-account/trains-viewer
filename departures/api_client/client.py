import requests
import configparser
import logging

# Get an instance of a logger
logger = logging.getLogger('django')

def readConfig():
    config = configparser.ConfigParser()
    config.read('departures/config.properties')
    return config

class StationNotFoundError(Exception):
    pass


class OcpAPIClient:

    den_haag_centraal_name = 'Den Haag Centraal'
    den_haag_centraal_code = 'GVC'
    train_categories = {'SPR': 'Sprinter', 'IC': 'Intercity'}
    config = readConfig()
    get_station_url = config['Endpoints']['get_station_url']
    get_depart_url = config['Endpoints']['get_depart_url']
    auth_headers = {config['Credentials']['key']: config['Credentials']['password']}

    def get_all_stations(self):
        logger.info('Inside web client, calling target web service to get all stations')
        resp_json = requests.get(self.get_station_url, headers=self.auth_headers).json()
        #logger.info('Got the Below Response: ')
        #logger.info(resp_json)
        stations = [{
            'name': station.get('namen').get('lang'),
            'code': station.get('code')}
            for station in resp_json.get('payload')]
        return stations

    def get_station_code(self, station_name=None):
        logger.info('Inside web client, fetching station code')
        # Default to 'Den Haag Centraal'
        station_name = station_name or self.den_haag_centraal_name
        all_stations = self.get_all_stations()
        result_list = [station for station in all_stations if station.get('name') == station_name]
        if len(result_list) < 1:
            raise StationNotFoundError('Station not found')
        else:
            return result_list[0].get('code')

    def get_departures(self, station_code=None):
        logger.info('Inside web client, calling target web service to get all departures')
        # Default to 'Den Haag Centraal'
        station_code = station_code or self.den_haag_centraal_code
        resp_json = requests.get(
            self.get_depart_url, params={'station': station_code}, headers=self.auth_headers).json()
        if 'payload' not in resp_json:
            raise StationNotFoundError
        departures = resp_json.get('payload').get('departures')
        result = []
        for departure in departures:
            result.append({
                'planned_departure_time': departure.get('plannedDateTime'),
                'direction': departure.get('direction'),
                'platform': departure.get('plannedTrack'),
                'train_type': self.train_categories.get(departure.get('trainCategory')),
            })
        return result