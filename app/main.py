import requests
import os

from dotenv import load_dotenv


def get_weather() -> None:
    load_dotenv()
    api_key = os.getenv("API_KEY")

    if not api_key:
        print("Error: API_KEY environment variable is not set.")
        return

    base_url = "http://api.weatherapi.com/v1/current.json"
    city = "Kyiv"

    try:
        response = requests.get(base_url, params={"key": api_key, "q": city})
        response.raise_for_status()
        data = response.json()

        print(f'Current weather in {data["location"]["name"]}: ')
        print(f'Temperature: {data["current"]["temp_c"]}°C')
        print(f'Condition: {data["current"]["condition"]["text"]}')

    except Exception as err:
        print(f"An error occurred: {err}")


if __name__ == "__main__":
    get_weather()
