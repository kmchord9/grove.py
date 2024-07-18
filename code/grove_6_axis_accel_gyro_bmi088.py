#!/usr/bin/env python
#
# This is the code for Grove - 6-Axis Accelerometer&Gyroscope (BMI088).
# (https://www.seeedstudio.com/Grove-6-Axis-Accelerometer-Gyroscope-BMI08-p-3188.html)
# which is a 6 DoF(degrees of freedom) High-performance Inertial Measurement Unit(IMU),
# based on BOSCH BMI088.
#
# @author Peter Yang <turmary@126.com>
#
# Grove.py is the library for Grove Base Hat which used to
# connect grove sensors for raspberry pi.
#
'''
## License

The MIT License (MIT)

Grove Base Hat for the Raspberry Pi, used to connect grove sensors.
Copyright (C) 2018  Seeed Technology Co.,Ltd. 

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

'''
from grove.grove_6_axis_accel_gyro_bmi088 import GroveAccelGyroBMI088

def main():
    import time

    snr = GroveAccelGyroBMI088()
    while True:
        tm = snr.get_sensor_time()
        # don't ask me why 26000, it's magic.
        print("Sensor time: {:.2f} S".format(tm / 26000.0))
        x, y, z = snr.get_accel()
        print(" AX = %7.2f mg  AY = %7.2f mg  AZ = %7.2f mg" % (x, y, z))
        x, y, z = snr.get_gyro()
        print(" GX = %7.2f dps GY = %7.2f dps GZ = %7.2f dps" % (x, y, z))
        time.sleep(2.0)

if __name__ == '__main__':
    main()
