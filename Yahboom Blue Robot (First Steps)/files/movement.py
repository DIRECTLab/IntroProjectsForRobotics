import RPi.GPIO as GPIO
import time

#Definition of  motor pin

IN1 = 20
IN2 = 21
IN3 = 19
IN4 = 26
ENA = 16
ENB = 13

#Set the GPIO port to BCM encoding mode

GPIO.setmode(GPIO.BCM)

#Ignore warning information

GPIO.setwarnings(False)



#Motor pin initialization operation

def motor_init():

    global pwm_ENA

    global pwm_ENB

    global delaytime

    GPIO.setup(ENA,GPIO.OUT,initial=GPIO.HIGH)
    GPIO.setup(IN1,GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(IN2,GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(ENB,GPIO.OUT,initial=GPIO.HIGH)
    GPIO.setup(IN3,GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(IN4,GPIO.OUT,initial=GPIO.LOW)

    #Set the PWM pin and frequency is 2000hz

    pwm_ENA = GPIO.PWM(ENA, 2000)

    pwm_ENB = GPIO.PWM(ENB, 2000)

    pwm_ENA.start(0)

    pwm_ENB.start(0)



#advance

def run(delaytime):

    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)

    pwm_ENA.ChangeDutyCycle(50)
    pwm_ENB.ChangeDutyCycle(50)

    time.sleep(delaytime)



#back

def back(delaytime):

    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)
    
    pwm_ENA.ChangeDutyCycle(50)
    pwm_ENB.ChangeDutyCycle(50)

    time.sleep(delaytime)



#turn left

def left(delaytime):

    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)

    pwm_ENA.ChangeDutyCycle(50)
    pwm_ENB.ChangeDutyCycle(50)

    time.sleep(delaytime)



#turn right
def right(delaytime):

    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.LOW)

    pwm_ENA.ChangeDutyCycle(50)
    pwm_ENB.ChangeDutyCycle(50)

    time.sleep(delaytime)



#turn left in place

def spin_left(delaytime):

    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)

    pwm_ENA.ChangeDutyCycle(50)
    pwm_ENB.ChangeDutyCycle(50)

    time.sleep(delaytime)



#turn right in place
def spin_right(delaytime):

    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)

    pwm_ENA.ChangeDutyCycle(50)
    pwm_ENB.ChangeDutyCycle(50)

    time.sleep(delaytime)

#brake
def brake(delaytime):

    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.LOW)

    pwm_ENA.ChangeDutyCycle(50)
    pwm_ENB.ChangeDutyCycle(50)

    time.sleep(delaytime)


if __name__ == "__main__":
    
    try:

        motor_init()

        # TODO: Write controls to get the robot to drive in a 5x5 box. The above code is provided
        # and should be able to be designed to do just that
        



    except KeyboardInterrupt:
        pass

    pwm_ENA.stop()

    pwm_ENB.stop()

    GPIO.cleanup()