#!/usr/bin/env python3
# -- coding: utf-8 --
import time

import RPi.GPIO as GPIO


# Set function to calculate percent from angle
def angle_to_percent(angle):
    if angle > 180 or angle < 0:
        return False

    start = 4
    end = 12.5
    ratio = (end - start) / 180  # Calcul ratio from angle to percent

    angle_as_percent = angle * ratio

    return start + angle_as_percent


GPIO.setmode(GPIO.BOARD)  # Use Board numerotation mode
GPIO.setwarnings(False)  # Disable warnings

# Use pin 12 for PWM signal
pwm_gpio = 12
frequence = 50
GPIO.setup(pwm_gpio, GPIO.OUT)
pwm = GPIO.PWM(pwm_gpio, frequence)

# Init at 0°
pwm.start(angle_to_percent(90))
time.sleep(1)

# Go at 25°
pwm.ChangeDutyCycle(angle_to_percent(75))
time.sleep(10)

# Go at 35°
pwm.ChangeDutyCycle(angle_to_percent(60))
time.sleep(10)

# Return 0°
pwm.ChangeDutyCycle(angle_to_percent(90))
time.sleep(1)

# Close GPIO & cleanup
pwm.stop()
GPIO.cleanup()