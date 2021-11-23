#!/usr/bin/python3
#
# 2021-11-06
#
# Rasperry Pi Model B Revision 2.0 (512MB)
# PCB comment : Pi 2011.12
#
# Connect WS2812B Addressable RGB LED to GPIO18 (PWM)
#
# Retrieve P1 meter data from WEB API , JSON string
# depending on the value of the Active Power consumprion in Watt 
# color the LED
#
# Note: this can only run under root priviliges
#   so run the script with sudo ...
#

import json
import requests
import time
import board
import neopixel

pixels = neopixel.NeoPixel(board.D18,1)
pixels.brightness = 0.1

DEBUG=0
FLIP=0

while True:
  r = requests.get('http://192.168.0.156/api/v1/data')
  packages_json = r.json()

  #t1 = packages_json['total_power_import_t1_kwh']
  #t2 = packages_json['total_power_import_t2_kwh']
  ap = packages_json['active_power_w']
  #gas = packages_json['total_gas_m3']

  #packages_str = json.dumps(packages_json, indent=2)
  #if(DEBUG):
  #  print(packages_str)

  if(DEBUG):
    #print('T1 kWh: ',t1)
    #print('T2 kWh: ',t2)
    print('Active Power: ',ap)
    #print('Total  Gas  : ',gas)
    #print('')

  if(ap<500):
    if(DEBUG):
      print('<500 => BLUE')
    pixels[0] = (0,0,255)
  elif(ap<1000):
    if(DEBUG):
      print('<1000 => GREEN')
    pixels[0] = (0,255,0)
  elif(ap<1500):
    if(DEBUG):
      print('<1500 => CHARTREUSE')
    pixels[0] = (127,255,0)
  elif(ap<2000):
    if(DEBUG):
      print('<2000 => YELLOW')
    pixels[0] = (255,255,0)
  elif(ap<3000):
    if(DEBUG):
      print('<3000 => ORANGE')
    pixels[0] = (255,127,0)
  else:
    if(DEBUG):
      print('>3000 => RED')
    pixels[0] = (255,0,0)

  if(FLIP==0):
    pixels.brightness = 0.01
    FLIP=1
  else:
    pixels.brightness = 0.1
    FLIP=0

  time.sleep(1)


