import requests


def get_weather(city_name, api_key):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric'

    response = requests.get(url)

    data = response.json()

    if response.status_code == 200:

        weather_info = {

            'city': data['name'],

            'temperature': data['main']['temp'],

            'description': data['weather'][0]['description']

        }

        return weather_info

    else:

        return None


def main():
    city = input("Enter city name: ")

    api_key = "2606f769271b8d545fe3458b2b72ed9f"

    weather = get_weather(city, api_key)

    if weather:

        print(f"Weather in {weather['city']}:")

        print(f"Temperature: {weather['temperature']}°C")

        print(f"Description: {weather['description']}")

    else:

        print("Failed to fetch weather information.")


if __name__ == "__main__":
    main()