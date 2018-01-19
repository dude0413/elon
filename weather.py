import forecastio
from package.config import dark_sky_key
from geopy.geocoders import Nominatim
from package.config import default_address

def get_weather(location, mode='hourly'):
    geolocator = Nominatim()
    # Get latitude and longitude #
    geolocation = geolocator.geocode(location)
    lat = geolocation.latitude
    long = geolocation.longitude
    forecast = forecastio.load_forecast(dark_sky_key, lat, long)
    # Hourly vs Daily Outcomes #
    if mode == 'hourly':
        sentence = 'Hourly Forecast for ' + str(geolocation) + ': ' + forecast.hourly().summary
        output = sentence
    elif mode == 'daily':
        print('Daily Forecast for: ' + str(geolocation) + ': ' + forecast.daily().summary)

# Get hourly weather for default address #
def default_weather():
    geolocator = Nominatim()

    geolocation =geolocator.geocode(default_address)
    lat = geolocation.latitude
    lng = geolocation.longitude
    forecast = forecastio.load_forecast(dark_sky_key, lat, lng)
    sentence = 'Hourly Forecast for ' + str(geolocation) + ': ' + forecast.hourly().summary
    print(sentence)


