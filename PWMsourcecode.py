# Code that changes PWM with time
#---------------------------------
import RPi.GPIO as GPIO
from time import sleep

Voltage = 10
duty=0		#50% duty cycle
ledpin = 12				# PWM pin connected to LED
GPIO.setwarnings(False)			#disable warnings
GPIO.setmode(GPIO.BOARD)		#set pin numbering system
GPIO.setup(ledpin,GPIO.OUT)
pi_pwm = GPIO.PWM(ledpin,1000)		#create PWM instance with frequency
pi_pwm.start(0)				#start PWM of required Duty Cycle 
while True:
	# Two-Point Calibration
	# Corrected_Value = (Raw_Value - Raw_Low)*Reference_Range/Raw_Range + Reference_Low
	duty = (Voltage - 9)*(100-0)/(12-9) + 0
    pi_pwm.ChangeDutyCycle(duty) # Fixed pwm
	pi_pwm.start(duty)
	print(duty)
	
	'Other Useful Functions'
	'pi_pwm.changeFrequency(f)'
	'pi_pwm.stop()'
	
	# Changing PWM
	# ------------
	# for duty in range(0,101,1):
        # pi_pwm.ChangeDutyCycle(duty) #provide duty cycle in the range 0-100
        # sleep(0.01)
    # sleep(0.5)
    
    # for duty in range(100,-1,-1):
        # pi_pwm.ChangeDutyCycle(duty)
        # sleep(0.01)
    # sleep(0.5)
	