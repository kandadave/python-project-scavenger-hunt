from art import text2art

def validate_location(location):
    return bool(location and location.strip()), None

def draw_ascii_map(location):
    return text2art(f"{location} Map", font="small")