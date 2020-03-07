from time import sleep
from datetime import datetime
from picamera import PiCamera
import sys
import RPi.GPIO as GPIO
class Photo():
    def __init__(self):
        self.__file ='/media/usb/'
        self.__filename = 'image'
        self.__extension = '.jpg'
	GPIO.setmode(GPIO.BCM)
    def createfile(self):
        now = datetime.now()
        timestampStr = now.strftime("%Y%m%d%H%M%S%f")
        totalfile = self.__file + self.__filename + timestampStr + self.__extension
        return totalfile
    def takefoto(self):
        count = 0
	camera = PiCamera()
        camera.led = False
	camera.start_preview(alpha=100)
	sleep(2)
	GPIO.setup(18, GPIO.OUT)
	GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        print('   Press Ctrl & C to Quit')

      	last_minute=0
	try:
    		while True:
			input_state = GPIO.input(17)
	     		if  input_state == False:
			  	sys.exit()
                        else:
                        	curr_minute = datetime.now().minute
       				sleep(1)
       				if curr_minute == last_minute:
           			 	pass
       			 	else:
          	    			camera.capture(self.createfile())
            				GPIO.output(18, True)
	    				sleep(0.3)
            				GPIO.output(18, False)
					print('picture number  : ' + str(count))
            				count += 1  # This is the same as count = count + 1
            				last_minute=curr_minute
	                        sleep(0.1)
                camera.stop_preview()
	except KeyboardInterrupt:
 	  print('Quit')
 	  GPIO.cleanup()
   	  camera.stop_preview()


miPhoto=Photo()
print(miPhoto.takefoto())
