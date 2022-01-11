# energy
Python Scripts to retrieve actual energy consumption from P1 Meter (HomeWizard)

More info on P1 meter can be found on :
 https://www.homewizard.nl/energy

 API HomeWizard WiFi P1 Meter
 https://homewizard-energy-api.readthedocs.io/

 The /api/v1/data endpoint always returns the most recent measurement.
 The update frequency depends on the device and, in case of the HWE-P1,
 the smart meter that it is connected to.
 With a SMR 5.0 meter, this is every second for power and every 5 minutes for gas.


<h2>01_json.py</h2>
   Decode the JSON string which is returned from the P1 meter https interface

<h2>02_influxdb.py</h2>
   Idem as 01 , but now inject this data in an Influx DB run on another machine<BR>
   Dependency on influxdb python library.<br>
   <br> 
   Install this influxdb library for python3 with following command:<BR>
   $ pip install influxdb
   <br>
   The script is called each minute from a crob jon on a computer in the same subnet.<br>
   <br>
   crontab -e<BR>
       # m h  dom mon dow   command <BR>
       * * * * * /home/jan/git/energy/02_influxdb.py

 
<h2>03_led.py</h2>
   Idem as 01 , but now the data of the actual power consumption is used to color an addressable WS2812B LED
   connected to a Raspberry PI.<BR>
     * Blue = low power consumption<BR> 
     * Green <BR>
     * Yellow<BR>
     * Red = high power consumption<BR>
   LED color status is updated every X seconds
