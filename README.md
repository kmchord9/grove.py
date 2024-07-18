![](https://user-images.githubusercontent.com/4081906/55451417-67559d00-5605-11e9-96b3-4c6bdd3e770c.png)

grove.py
========

[![Build Status](https://travis-ci.org/Seeed-Studio/grove.py.svg?branch=master)](https://travis-ci.org/Seeed-Studio/grove.py)
[![](https://img.shields.io/pypi/v/grove.py.svg)](https://pypi.python.org/pypi/grove.py)

Python library for Seeedstudio Grove Devices on embeded Linux platform, especially good on below platforms:
- [Coral Dev Board](https://www.seeedstudio.com/Coral-Dev-Board-p-2900.html) [(Wiki)](http://wiki.seeedstudio.com/Grove_Base_Hat_for_Raspberry_Pi/#software)
- [NVIDIA Jetson Nano](https://www.seeedstudio.com/NVIDIA-Jetson-Nano-Development-Kit-p-2916.html) [(Wiki)](http://wiki.seeedstudio.com/Grove_Base_Hat_for_Raspberry_Pi/#software)
- [Raspberry Pi](https://www.seeedstudio.com/category/Boards-c-17.html) [(Wiki)](http://wiki.seeedstudio.com/Grove_Base_Hat_for_Raspberry_Pi/#software)

<br><br>
# Architecture
To operate grove sensors, the grove.py depends on the smbus2 hardware interface library.

<br>

![](images/grove-py-arch.png)

<br><br>
# Installation
For beginner or library user only, please install with online method.<br>
For developer or advanced user, please install [dependencies](doc/INSTALL.md#install-dependencies)
and then install grove.py with [source code](#install-grovepy).

### Caution

Here is the compatibility of [grove.py](https://github.com/Seeed-Studio/grove.py) with Python2 and Python3 on each releases of Raspbian/Raspberry Pi OS.

| Raspberry Pi OS Releases | grove.py for Python2 | grove.py for Python3 |
| ---- | ---- | ---- |
| 9 (Stretch) | √ | √ |
| 10 (Buster) until 2020-08-20 | √ | √ |
| 10 (Buster) after 2020-08-20 | × | √ |
| 11 (Bullseye) | × | √ |
| 12 (bookworm) | × | √ |

**Because Python2 is obsolete and APT repository does not provide `python-pip`, so the Raspberry Pi OS releases which after `10 (Buster) 2020-08-20` cannot use `Online install` command. We also recommend using Python3 to all the users and developers.**

### Install grove.py

```
git clone https://github.com/kmchord9/grove.py.git
cd grove.py
python -m venv vgrove
source vgrove/bin/activate
pip install .
```

<br><br>
## Usage

![](https://files.seeedstudio.com/wiki/Grove_Base_Hat_for_Raspberry_Pi/img/pin-out/overview.jpg)
Grove Base Hat for Raspberry Piのピン配置は上記の画像のようになっており、  
センサーの仕様によってDigital,Analog,I2C,PWM,UARTの接続先が異なるので注意する。

### 温度センサー（DHT22）
接続先 Digital  
![image](https://github.com/user-attachments/assets/81509f75-8e44-4bc4-96da-1846fb79e203)  
[Gravity- DHT22 温湿度センサ — スイッチサイエンス](https://www.switch-science.com/products/5020?_pos=1&_sid=c8d6ee23d&_ss=r)

#### 依存ライブラリのインストール
```
sudo apt-get install libgpiod2
pip install adafruit-circuitpython-dht
```
#### 実行方法
```
cd grove.py/code
python grove_temperature_dht22.py 18
```
D18に接続した場合には引数に18を入れる

### 距離センサ
接続先 Digital  
![image](https://github.com/user-attachments/assets/e355019d-ae1a-4199-a8ee-72b17543889a)  
[GROVE - 超音波距離センサモジュール — スイッチサイエンス](https://www.switch-science.com/products/1383)
#### 依存ライブラリのインストール
```

```
#### 実行方法
```
cd grove.py/code
python grove_ultrasonic_ranger.py 18
```
D18に接続した場合には引数に18を入れる

### 振動センサ
接続先 Digital  
![image](https://github.com/user-attachments/assets/2e99fead-ef3a-4805-9944-fdca92dd61f0)  
[GROVE - 振動センサ（SW-420） — スイッチサイエンス](https://www.switch-science.com/products/5347?_pos=3&_sid=2162527a3&_ss=r)
#### 依存ライブラリのインストール
```
pip install pigpio
pip install gpiozero
```
#### 実行方法
```
cd grove.py/code
python grove_vibration_sw420.py 18
```
D18に接続した場合には引数に18を入れる

### 6軸加速度・ジャイロセンサ(BMI088)
接続先 I2C  
![image](https://github.com/user-attachments/assets/f073a62f-01bb-4e34-a660-c6605b6345bb)  
[GROVE - 6軸加速度・ジャイロセンサ（BMI088） — スイッチサイエンス](https://www.switch-science.com/products/5343?_pos=1&_sid=37a2f6032&_ss=r)  

#### 依存ライブラリのインストール
```
sudo apt-get install debhelper dh-make debmake devscripts fakeroot
cd ~
git clone https://github.com/turmary/bmi088-python.git
cd bmi088-python
git submodule init
git submodule update
./tools/packaging_deb.sh
cd ~/bmi088-python/deobj
sudo dpkg -i libbmi088_0.0.2-1_arm64.deb
```
[bmi088-python/ at master · turmary/bmi088-python](https://github.com/turmary/bmi088-python/tree/master)

#### 実行方法
```
cd grove.py/code
python grove_6_axis_accel_gyro_bmi088.py
```

### 音センサ
接続先 Analog  
![image](https://github.com/user-attachments/assets/b950d463-7a64-4cd6-ac19-c46cf5578281)  

[Gravity- DHT22 温湿度センサ — スイッチサイエンス](https://www.switch-science.com/products/5020?_pos=1&_sid=c8d6ee23d&_ss=r)
#### 依存ライブラリのインストール
```

```
#### 実行方法
```
cd grove.py/code
python grove_sound_sensor.py 0
```
A0に接続した場合には引数に0を入れる


<br><br>
## API Documentation
click [here](https://seeed-studio.github.io/grove.py)

[how to update me](sphinx/README.md)

<br><br>
## Contribution
Check list for adding a new grove device, for simple, take [grove_led](grove/grove_led.py) as a example.
- Add a Class in the python source file, and export with `__all__ =`
- Code sytle [PEP8](https://www.python.org/dev/peps/pep-0008) is recommanded
- The python source could run directly with `python <file>` and `python3 <file>`
- Add demo code at the near top of source file
- The demo code could run directly with someone python/python3 IDE.
- Add document to class and it's member and show the result by refering to [API document](#api-documentation)
- Add a command item in setup.py `console_scripts` list, take effect by [install again](#install-grovepy)
- Add a item to command table in [Usage Doc](doc/README.md)
- If the command need argument but not specified, please list available arguments.
- If specified invalid argument, also output usage document then exit.
