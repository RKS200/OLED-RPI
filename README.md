# OLED-RPI
A try to make oled display as usable as possible.
you need [adafriut ssd1306](https://learn.adafruit.com/monochrome-oled-breakouts/python-setup) before installing.

The script is made for ssd1306 128x64 Display only.
## Installation
Download the project.
~~~bash
sudo apt install git -y
git clone "https://github.com/RKS200/OLED-RPI.git"
~~~
Editing rc.local for startup at boot.
~~~bash
sudo nano /etc/rc.local
~~~
then add the below line above exit 0.
~~~bash
python3 <full path>/oled.py
~~~
Make rc.local executable.
~~~bash
sudo chmod +x /etc/rc.local
~~~
Now reboot the system and Hope the display will work😂.
---
![main](https://github.com/RKS200/OLED-RPI/blob/main/1.jpeg)
![startup](https://github.com/RKS200/OLED-RPI/blob/main/2.jpeg)
