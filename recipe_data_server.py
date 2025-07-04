# mealDB API
# https://www.themealdb.com/api.php
import requests
from requests.exceptions import Timeout
import json     # for pretty print
from tst7_zeromq_send_020324_v07 import send_message


def get_data(timeout=5):
    """
    Get meal data from the mealDB API
    :param timeout: timeout for the request
    :return: meal data as JSON
    """
    # API URL
    url = 'https://www.themealdb.com/api/json/v1/1/list.php?i=list'
    try:
        # Get data from API
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()  # Raises stored HTTPError, if one occurred.
    except Timeout:
        print(f"Timeout occurred for url: {url}")
        return None
    except requests.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        return None
    except Exception as err:
        print(f"An error occurred: {err}")
        return None
    else:
        print(response.status_code)
        # data is JSON
        data = response.json()
        # return data
        return data


if __name__ == '__main__':
    # Test the function

    # send_message(get_data())    # get meal data and send it using zeroMQ
    print(get_data())     # get meal data. For Jacky's individual project
    print("Done")
