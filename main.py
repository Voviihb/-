import sys
from io import BytesIO
# import pprint
import requests
from PIL import Image
from scale import get_scale

# python main.py Москва, ул. Ак. Королева, 12
toponym_to_find = " ".join(sys.argv[1:])
# toponym_to_find = "Москва, ул. Ак. Королева, 12"

geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"

geocoder_params = {
    "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
    "geocode": toponym_to_find,
    "format": "json"}

response = requests.get(geocoder_api_server, params=geocoder_params)

if not response:
    pass
else:
    # print(response)
    json_response = response.json()
    # pprint.pprint(json_response)
    toponym_longitude, toponym_lattitude, delta_long, delta_lat = get_scale(json_response)
    map_params = {
        "ll": ",".join([toponym_longitude, toponym_lattitude]),
        "spn": ",".join([delta_long, delta_lat]),
        "pt": f"{toponym_longitude},{toponym_lattitude},pm2rdm",
        "l": "map"
    }

    map_api_server = "http://static-maps.yandex.ru/1.x/"
    response = requests.get(map_api_server, params=map_params)
    # print(response.url)

    Image.open(BytesIO(
        response.content)).show()
