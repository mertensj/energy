#!/usr/bin/python3
#
# https://www.homewizard.nl/energy
#
# API HomeWizard WiFi P1 Meter
# https://homewizard-energy-api.readthedocs.io/
#
# The /api/v1/data endpoint always returns the most recent measurement.
# The update frequency depends on the device and, in case of the HWE-P1, 
# the smart meter that it is connected to. 
# With a SMR 5.0 meter, this is every second for power and every 5 minutes for gas.
#

import json
import requests

r = requests.get('http://192.168.0.156/api/v1/data')
packages_json = r.json()

package_t1 = packages_json['total_power_import_t1_kwh']
package_t2 = packages_json['total_power_import_t2_kwh']
package_power = packages_json['active_power_w']
package_gas = packages_json['total_gas_m3']

packages_str = json.dumps(packages_json, indent=2)

print('T1 kWh: ',package_t1)
print('T2 kWh: ',package_t2)
print('Active Power: ',package_power)
print('Total  Gas  : ',package_gas)
print('')
print(packages_str)

