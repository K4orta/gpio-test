#!/usr/bin/env python

import RPi.GPIO as GPIO, time

GPIO.setmode(GPIO.BCM)
GREEN_LED = 18
RED_LED = 23
GPIO.setup(GREEN_LED, GPIO.OUT)
GPIO.setup(RED_LED, GPIO.OUT)
red_state = False
green_state = True

while True:
  red_state = !red_state
  green_state = !green_state
  GPIO.output(GREEN_LED, green_state)
  GPIO.output(RED_LED, red_state)
  time.sleep(1)

