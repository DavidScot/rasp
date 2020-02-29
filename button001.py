from time import sleep
from datetime import datetime
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
print('   Press Ctrl & C to Quit')
try:
	while True:
     		if GPIO.input(17):
    			GPIO.output(18, False)
      		else:
      			GPIO.output(18, True)
                sleep(0.1)
except KeyboardInterrupt:
  print('Quit')
  GPIO.cleanup()

