#!/usr/bin/python

# This program is to convert the band gap to the wavelength corresponding light.


import math
gap=float(input('Please input the gap(in ev) '))

ee=1.60217662 *10**-19 # elementary charge
cc=299792458.0  # speed of light
hh=6.62607004*10**-34  #Planck's constant

wl=hh*cc/gap/ee *10**9 # in nano meters

print 'the wavelength (in nm) of the corresponding light is ', wl
