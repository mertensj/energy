# energy
Python Scripts to retrieve actual energy consumption from P1 Meter (HomeWizard)
<h2>01_json.py</h2>
   Decode the JSON string which is returned from the P1 meter https interface
<h2>02_influxdb.py</h2>
   Idem as 01 , but now inject this data in an Influx DB run on another machine<BR>
   This script is called each minute from a crob jon on a raspberry PI
<h2>03_led.py</h2>
   Idem as 01 , but now the data of the actual power consumption is used to color an addressable WS2812B LED
   connected to a Raspberry PI.<BR>
     * Blue = low power consumption<BR> 
     * Green <BR>
     * Yellow<BR>
     * Red = high power consumption<BR>
   LED color status is updated every X seconds
