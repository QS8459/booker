from math import (
    sin,
    pi,
    sqrt,
    cos,
    atan2
)


def calculate_distance(
        lat1: float,
        lat2: float,
        lon1: float,
        lon2: float
):
    earth_R: int = 6371 #in km
    difference_lat = deg2rad(lat2-lat1)
    difference_lon = deg2rad(lon2-lon1)

    a = sin(difference_lat/2) * sin(difference_lat/2) + \
        cos(deg2rad(lat1)) * cos(deg2rad(lat2)) * \
        sin(difference_lon/2) * sin(difference_lon/2)

    c = 2 * atan2(sqrt(a), sqrt(1-a))
    return earth_R * c


def deg2rad(deg):
    return deg * (pi/180)
