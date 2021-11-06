#!/usr/bin/python3
# Use P1 meter API
#   API HomeWizard WiFi P1 Meter
#   https://homewizard-energy-api.readthedocs.io/
# Fetch all JSON data
# inject into InfluxDB V1 running on computer 'compaq.local'
#
# A single line of text in line protocol format represents one data point in InfluxDB. 
# It informs InfluxDB of the point’s measurement, tag set, field set, and timestamp.
# - measurement : log
# - tag set     : sensor=P1
# - field set   : t1 / t2 / ap / gas
#        t1 = DAY counter , cummulative in kWh
#        t2 = NIGHT counter , cummulative in kWh
#        ap = activer power in Watt
#        gas = cummulative gas counter in m3
#

import json
import requests
from influxdb import InfluxDBClient

DEBUG=0

r = requests.get('http://192.168.0.156/api/v1/data')
packages_json = r.json()

package_t1 = packages_json['total_power_import_t1_kwh']
package_t2 = packages_json['total_power_import_t2_kwh']
package_power = packages_json['active_power_w']
package_gas = packages_json['total_gas_m3']

packages_str = json.dumps(packages_json, indent=2)

if(DEBUG):
  print('T1 kWh: ',package_t1)
  print('T2 kWh: ',package_t2)
  print('Active Power: ',package_power)
  print('Total  Gas  : ',package_gas)
  print('')

if(DEBUG):
  print(packages_str)

client = InfluxDBClient(host='compaq.local', port=8086)
if(DEBUG):
  print(client.get_list_database())

#client.switch_database('energydb')

line = 'log,sensor=P1 ' + \
       't1=' + str(package_t1) + \
       ',t2=' + str(package_t2) + \
       ',ap=' + str(package_power) + \
       ',gas=' + str(package_gas)

client.write([line], {'db': 'energydb'}, 204, 'line')
client.close()


