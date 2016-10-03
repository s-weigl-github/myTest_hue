# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 17:44:37 2016

@author: techadmin

first attempt using python with philips hue

"""

from phue import Bridge

b = Bridge('192.168.61.21')

b.connect()

b.get_api()

b.get_light(1, 'on')

b.set_light(1, 'bri', 254)

b.set_light(2, 'bri', 127)

b.set_light(2, 'on', True)

b.set_light([1,2], 'on', True)

b.get_light(1, 'name')

b.get_light('flur')
b.set_light('flur', 'bri', 254)

b.set_light(['flur', 'zimmer'], 'on', False)

command = {'transitiontime' : 300, 'on' : True, 'bri' : 254}
b.set_light(1, command)
