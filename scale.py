def get_scale(json_response):
    toponym = json_response['response']["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
    toponym_coodrinates = toponym["Point"]["pos"]
    toponym_lowerCorner_coordinates = toponym["boundedBy"]["Envelope"]["lowerCorner"].split()
    toponym_upperCorner_coordinates = toponym["boundedBy"]["Envelope"]["upperCorner"].split()
    toponym_longitude, toponym_lattitude = toponym_coodrinates.split(" ")
    delta_long = str(abs(float(toponym_lowerCorner_coordinates[0]) - float(toponym_upperCorner_coordinates[0])))
    delta_lat = str(abs(float(toponym_lowerCorner_coordinates[1]) - float(toponym_upperCorner_coordinates[1])))
    return toponym_longitude, toponym_lattitude, delta_long, delta_lat
