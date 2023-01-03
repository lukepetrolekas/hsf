# goog api
from typing import List
import re


# vars
base_url = 'https://www.google.com/maps/search/?api=1'

# add any encoding rules here
str_encoding_mapping = {
	'%': '%25',
	' ': '+',
	',': '%2C',
	'"': '%22',
	'<': '%3C',
	'>': '%3E',
	'#': '%23',
	'|': '%7C',
}


# utils
def validate_coord()
	return NotImplemented

def str_enc(str_to_encode: str, str_map: dict = str_encoding_mapping) -> str:
	# String replacement needs to be done in 1 pass, rather in a loop to avoid weird side effects
	# >> str_enc('City Hall, New York, NY')
	# >> 'City+Hall%2C+New+York%2C+NY'
	foo = re.sub('.', lambda m: str_map.get(m.group(), m.group()), str_to_encode)
	return foo


# search
def maps_url_search(query: str, base: str = base_url):
	# query: 	can be a (place name, address, comma-separated latitude/longitude coordinates)
	# >> maps_url_search('City Hall, New York, NY')
	# >> 'https://www.google.com/maps/search/?api=1&query=City+Hall%2C+New+York%2C+NY'
	query_enc = str_enc(query)
	url = f"{base}&query={query_enc}"
	return url


# TODO: directions
def maps_url_directions(origin: str, destination: str, travelmode: str, waypoints: str):
	# N.b. all kwargs needs to be fed through str_enc()
	return NotImplemented


# TODO: display map
def maps_url_display_map(map_action: str):
	# N.b. all kwargs needs to be fed through str_enc()
	return NotImplemented


# TODO: street view
def maps_url_street_view(map_action: str = 'pano', viewpoint: str, pano: str):
	# N.b. all kwargs needs to be fed through str_enc()
	return NotImplemented


