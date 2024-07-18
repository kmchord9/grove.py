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
from gpiozero import Button
from gpiozero.pins.pigpio import PiGPIOFactory
from signal import pause

def main():
    from grove.helper import SlotHelper
    sh = SlotHelper()
    pin = sh.argv2pin()

    factory = PiGPIOFactory()
    snsr = Button(pin, bounce_time=0.01, pin_factory=factory)

    def detect_vibration():
        print("振動を検出！")

    snsr.when_pressed = detect_vibration

    pause()

    return

if __name__ == '__main__':
    main()