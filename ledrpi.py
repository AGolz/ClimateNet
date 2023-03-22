# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ledrpi.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: emaksimo <emaksimo@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/22 18:20:47 by emaksimo          #+#    #+#              #
#    Updated: 2023/03/22 18:20:49 by emaksimo         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

LED_PIN = 18

GPIO.setup(LED_PIN, GPIO.OUT)

GPIO.output(LED_PIN, GPIO.HIGH)

time.sleep(5)

GPIO.output(LED_PIN, GPIO.LOW)

GPIO.cleanup()
