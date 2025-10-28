import numpy as np
from math import radians, degrees, sin, cos, asin,atan2,sqrt

EARTH_RADIUS = 6371.0

def calculate_dis(x, y):
    x = np.radians(x) if np.max(x) > np.pi else x
    y = np.radians(y) if np.max(y) > np.pi else y

    dlat = y[0] - x[0]
    dlon = y[1] - x[1]

    a = np.sin(dlat / 2.0) ** 2 + np.cos(x[0]) * np.cos(y[0]) * np.sin(dlon / 2.0) ** 2
    c = 2 * np.arcsin(np.sqrt(a))

    km =  round((EARTH_RADIUS * c),2)
    mi = round((km * 0.621371),2)
    return {"miles" : mi, "kilometers" : km}

def calculate_coordinate_ranges(lat, lon, distance_km):

    earth_radius_km = 6371.0


    lat_rad = radians(lat)
    lon_rad = radians(lon)


    angular_distance = distance_km / earth_radius_km


    new_lat_min = degrees(lat_rad - angular_distance)
    new_lat_max = degrees(lat_rad + angular_distance)


    delta_lon = asin(sin(angular_distance) / cos(lat_rad))
    new_lon_min = degrees(lon_rad - delta_lon)
    new_lon_max = degrees(lon_rad + delta_lon)


    lat_range = (new_lat_min,new_lat_max)
    lon_range = (new_lon_min,new_lon_max)

    return (lat_range, lon_range)

def haversine(lat1, lon1, lat2, lon2):
    R = 6371


    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])


    dlat = lat2 - lat1
    dlon = lon2 - lon1


    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c

    return distance