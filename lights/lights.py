import requests,sys
from datetime import datetime
import pytz

def get_sunrise_sunset(latitude, longitude):
    try:
        url = f"https://api.sunrise-sunset.org/json?lat={latitude}&lng={longitude}&formatted=0&tzid=Europe/Amsterdam"
        response = requests.get(url)
        data = response.json()
        if 'results' in data:
            return data['results']
        else:
            return None
    except Exception as e:
        print("OFF") # Ensure lights are off when unable to call the API, this saves electricity :-)
        sys.exit()

def main():
    latitude = 50.930581
    longitude = 5.780691
    result = get_sunrise_sunset(latitude, longitude)
    if result:
        sunrise_time = datetime.strptime(result['sunrise'], "%Y-%m-%dT%H:%M:%S%z")
        sunset_time = datetime.strptime(result['sunset'], "%Y-%m-%dT%H:%M:%S%z")

        amsterdam_timezone = pytz.timezone('Europe/Amsterdam')
        current_time = datetime.now(amsterdam_timezone)

        if sunrise_time < current_time < sunset_time:
            print("OFF")
        else:
            print("ON")

    else:
        print("OFF") # Ensure lights are off when unable to parse results from the API, this saves electricity :-)

if __name__ == "__main__":
    main()
