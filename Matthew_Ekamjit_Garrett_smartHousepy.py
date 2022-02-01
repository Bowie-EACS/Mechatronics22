import mechatronics as mech
import time

# LED pin values
LED_1 = 14 
LED_2 = 15
LED_3 = 8
LED_4 = 7
LED_5 = 16
LED_6 = 20

mech.initialize_led(LED_1) # Initialize Led
mech.initialize_led(LED_2)
mech.initialize_led(LED_3)
mech.initialize_led(LED_4)
mech.initialize_led(LED_5)
mech.initialize_led(LED_6)


ON = 1
OFF = 0
right_LDR = 1 # channel
brightness = mech.read_ldr(right_LDR)
def lights_on(): #short on function for all LEDS 
    mech.set_led(LED_1, ON) 
    mech.set_led(LED_2, ON) 
    mech.set_led(LED_3, ON)
    mech.set_led(LED_4, ON)
    mech.set_led(LED_5, ON)
    mech.set_led(LED_6, ON)

def lights_off(): #short off function for all LEDS
    mech.set_led(LED_1, OFF) 
    mech.set_led(LED_2, OFF) 
    mech.set_led(LED_3, OFF)
    mech.set_led(LED_4, OFF)
    mech.set_led(LED_5, OFF)
    mech.set_led(LED_6, OFF)

def code_from_packet():
    while True: #ldr live feed
        brightness = mech.read_ldr(right_LDR)
        print("LDR Level is " + str(brightness))
        time.sleep(1)
    if brightness == 2.0: #conditionals
        time.step(8)
    elif (brightness < 3.0) and (brightness >= 2.49):
        time.step(2.5)    
    elif (brightness > 3.0) and (brightness < 3.3):
        time.step(0.1)

try:
    code_from_packet() 
except KeyboardInerrupt:
    lights_off() #turns lights off if try content doesn't work

"""

# basic run test for all LEDS that looks like a arcade/carnival game
i = 1
while i <= 20:
    mech.set_led(LED_1, ON)
    time.sleep(0.1)
    mech.set_led(LED_1, OFF)
    
    mech.set_led(LED_2, ON)
    time.sleep(0.1)
    mech.set_led(LED_2, OFF)
    
    mech.set_led(LED_3, ON)
    time.sleep(0.1)
    mech.set_led(LED_3, OFF)
    
    mech.set_led(LED_4, ON)
    time.sleep(0.1)
    mech.set_led(LED_4, OFF)
    
    mech.set_led(LED_5, ON)
    time.sleep(0.1)
    mech.set_led(LED_5, OFF)

    mech.set_led(LED_6, ON)
    time.sleep(0.1)
    mech.set_led(LED_6, OFF)
    
    i = i + 1
"""
