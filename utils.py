import settings

def height_percent(percent):
    return int(settings.HEIGHT * percent / 100)

def width_percent(percent):
    return int(settings.WIDTH * percent / 100)