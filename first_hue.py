##########################
### just the first attempt
### there will be more in no time
### i hope :-)
### covering the basics for now
##########################

from phue import Bridge
from time import sleep

b = Bridge(ip='192.168.61.2')

b.connect()

b.get_api()

b.set_light(['zimmer'], 'bri', 75) #75
sleep(2)
b.set_light(['flur', 'küche'], 'bri', 38) #38
b.set_light(['flur', 'zimmer', 'küche'], 'sat', 254)
b.set_light(['flur', 'zimmer', 'küche'], 'hue', 15000)


# E-o-F