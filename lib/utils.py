import geocoder
from art import text2art

def validate_location(location):
    try:
        g = geocoder.osm(location)
        return g.ok, g.latlng if g.ok else None
    except Exception:
        return False, None

def draw_ascii_map(location):
    return text2art(f"{location} Map", font="small")