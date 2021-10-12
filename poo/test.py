from geopy.geocoders import Nominatim

local: dict = {}
geolocator = Nominatim(user_agent="myGeocoder")
location = geolocator.reverse("-22.059065, -48.173027")
local = location.address
print(local)


# def coverte(latitudes):
#     local2 = []
#     geolocator2 = Nominatim(user_agent="myGeocoder")
#     location2 = geolocator2.reverse(latitudes)
#     local2 = location2.address.split()

#     return local2


# print(coverte("-22.059065, -48.173027"))
