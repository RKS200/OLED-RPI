import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306,time
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from datetime import datetime
import subprocess, psutil
import PIL.ImageOps

disp = Adafruit_SSD1306.SSD1306_128_64(rst = 0,i2c_address=0x3C)
disp.begin()
width = disp.width
height = disp.height
font = ImageFont.load_default()
image = Image.new('1', (width, height))
draw = ImageDraw.Draw(image)
draw.rectangle((0,0,width,height), outline=0, fill=1)
img = Image.open('/home/rks/Desktop/rpi.ppm')
img = PIL.ImageOps.invert(img).convert('1')
disp.image(img)
disp.display()
time.sleep(1)
while True:
	draw.rectangle((0,0,127,63), outline=1, fill=0)
	now = datetime.now()
	current_time = now.strftime("%H:%M:%S")
	draw.text((10,0),"Time: "+current_time,font=font, fill=255)
	temp = subprocess.run(["vcgencmd","measure_temp"],stdout=subprocess.PIPE).stdout.decode("utf-8").strip('\n').strip('temp=')
	draw.text((10,10),"Temp: "+temp,font=font, fill=255)
	cmd = "top -bn1 | grep load | awk '{printf \"CPU Load: %.2f\", $(NF-2)}'"
	CPU = str(psutil.cpu_percent()) + '%'
	freq = str(list(psutil.cpu_freq())[0])
	cmd = "free -m | awk 'NR==2{printf \"%.2f%%\",$3*100/$2 }'"
	MemUsage = subprocess.check_output(cmd, shell = True ).decode("utf-8")
	draw.text((10,20),"CPU : "+CPU,font=font, fill=255)
	draw.text((10,30),"Freq: "+freq,font=font, fill=255)
	draw.text((10,40),"RAM : "+MemUsage,font=font, fill=255)
	cmd = "hostname -I | cut -d\' \' -f1"
	IP = subprocess.check_output(cmd, shell = True ).decode("utf-8")
	draw.text((10,50),"IP  : "+IP,font=font, fill=255)
	disp.image(image)
	disp.display()
	time.sleep(.1)
