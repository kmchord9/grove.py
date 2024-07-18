#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# The MIT License (MIT)
#
# Grove Base Hat for the Raspberry Pi, used to connect grove sensors.
# Copyright (C) 2018  Seeed Technology Co.,Ltd.
'''
This is the code for
    - Grove 

Examples:

'''
import time
import board
import adafruit_dht
from adafruit_blinka.microcontroller.bcm283x.pin import Pin

def main():
    from grove.helper import SlotHelper
    sh = SlotHelper()
    pin = sh.argv2pin()
    pin_asn = Pin(pin)

    dhtDevice = adafruit_dht.DHT22(pin_asn)

    while True:
        try:
            # Print the values to the serial port
            temperature_c = dhtDevice.temperature
            humidity = dhtDevice.humidity

            print("Temp:  {:.1f} C    Humidity: {}% ".format(temperature_c, humidity))

        except RuntimeError as error:
            # Errors happen fairly often, DHT's are hard to read, just keep going
            print(error.args[0])
            time.sleep(2.0)
            continue
        except Exception as error:
            dhtDevice.exit()
            raise error     
            temperature_c = dhtDevice.temperature
            humidity = dhtDevice.humidity

        time.sleep(2)

if __name__ == '__main__':
    main()
