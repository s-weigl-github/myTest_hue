
from phue import Bridge

b = Bridge(ip='192.168.61.21')

b.connect()

b.get_api()

b.set_light(['zimmer'], 'bri', 100)
b.set_light(['flur', 'küche'], 'bri', 50)
b.set_light(['flur', 'zimmer', 'küche'], 'sat', 254)
b.set_light(['flur', 'zimmer', 'küche'], 'hue', 15000)
