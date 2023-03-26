import sys
import os
import time

sys.path.append(os.path.abspath("/home/pi/projects/grow-python"))

from library.grow.moisture import Moisture
from service.discord import send_to_discord

moisture1 = Moisture(1)  # Monitor channel 1

DRY_POINT = 27
WET_POINT = 1
moisture1.set_dry_point(DRY_POINT)
moisture1.set_wet_point(WET_POINT)

log = []

measurments = 0
moisture = 0

while measurments < 5:
  #wait for data stream
  if moisture1.new_data:
    time.sleep(1.0 / 60)

    measurments += 1

    moistureLevel = moisture1.moisture
    saturationLevel = moisture1.saturation

    moisture += moistureLevel

    print(f"Moisture level is: {moistureLevel}")
    print(f"Saturation level is: {saturationLevel}")


    #runs as a cron every 5 minutes
    if measurments == 5 and (moisture / 5) < 12.5:
     message = "My moisture level has dropped to {}".format(moisture / 5)
     print(message)

     #send_to_discord(message)