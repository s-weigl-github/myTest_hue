# -*- coding: utf-8 -*-

##########################
### just the first attempt
### there will be more in no time
### i hope :-)
### covering the basics for now
##########################

from phue import Bridge
from time import sleep

b = Bridge(ip='192.168.61.21')

b.connect()

b.get_api()

b.set_light(['küche'], 'bri', 80)
b.set_light(['küche'], 'sat', 45)
b.set_light(['küche'], 'hue', 235)


# E-o-F