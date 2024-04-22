# Write your code here :-)
"""CircuitPython Essentials Servo standard servo example"""
import time
import board
import pwmio
from adafruit_motor import servo

# create a PWMOut object on Pin A2.
pwm = pwmio.PWMOut(board.GP18, duty_cycle=2 ** 15, frequency=50)
pwm1 = pwmio.PWMOut(board.GP19, duty_cycle=2 ** 15, frequency=50)
pwm2 = pwmio.PWMOut(board.GP20, duty_cycle=2 ** 15, frequency=50)
pwm3 = pwmio.PWMOut(board.GP21, duty_cycle=2 ** 15, frequency=50)

# Create a servo object, my_servo.
my_servo0 = servo.Servo(pwm)
my_servo1 = servo.Servo(pwm1)
my_servo2 = servo.Servo(pwm2)
my_servo3 = servo.Servo(pwm3)

speed = 10

def move_hori_1():
    for angle in range(30, 180, speed):  # 0 - 180 degrees, 5 degrees at a time.
        my_servo0.angle = angle
        time.sleep(0.05)
    for angle in range(180, 30, speed * -1):  # 0 - 180 degrees, 5 degrees at a time.
        my_servo0.angle = angle
        time.sleep(0.05)

def move_hori_2():
    for angle in range(180, 30, speed * -1):  # 0 - 180 degrees, 5 degrees at a time.
        my_servo3.angle = angle
        time.sleep(0.05)
    for angle in range(30, 180, speed):  # 0 - 180 degrees, 5 degrees at a time.
        my_servo3.angle = angle
        time.sleep(0.05)

def move_ver_1():
    for angle in range(180, 0, speed*-1):  # 0 - 180 degrees, 5 degrees at a time.
        my_servo2.angle = angle
        time.sleep(0.05)
    my_servo2.angle = 30
    time.sleep(1)
def move_ver_2():
    for angle in range(180, 30, -15):  # 0 - 180 degrees, 5 degrees at a time.
        my_servo1.angle = angle
        time.sleep(0.05)
    my_servo1.angle = 150
    time.sleep(1)

def hug():
    for angle in range(30, 90, speed):  # 0 - 180 degrees, 5 degrees at a time.
        my_servo2.angle = angle
        my_servo1.angle = 180-angle
        time.sleep(0.05)
    time.sleep(0.5)

    for angle in range(30, 180, speed):  # 0 - 180 degrees, 5 degrees at a time.
        my_servo0.angle = angle
        my_servo3.angle = 180-angle
        time.sleep(0.05)
    time.sleep(1)
    for angle in range(180, 30, speed * -1):  # 0 - 180 degrees, 5 degrees at a time.
        my_servo0.angle = angle
        my_servo3.angle = 180-angle
        time.sleep(0.05)
    my_servo3.angle = 180
    time.sleep(0.3)

    for angle in range(90, 30, speed * -1):  # 0 - 180 degrees, 5 degrees at a time.
        my_servo2.angle = angle
        my_servo1.angle = 180-angle
        time.sleep(0.05)
    time.sleep(0.5)


def wave():
    my_servo1.angle = 30
    time.sleep(0.5)
    my_servo1.angle = 90
    time.sleep(0.3)
    my_servo1.angle = 30
    time.sleep(0.3)
    my_servo1.angle = 150
    time.sleep(0.5)

hug()
wave()
