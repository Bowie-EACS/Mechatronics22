"""
Jake and Tyler Parking Assistant
"""

import mechatronics as mech
import time
#mech.cleanup()

LED_FAR = 11
LED_MID = 9
LED_NEAR = 10

LED_FAR_O = 5
LED_MID_O = 6
LED_NEAR_O = 13

mech.initialize_led(LED_FAR)
mech.initialize_led(LED_MID)
mech.initialize_led(LED_NEAR)
mech.initialize_led(LED_FAR_O)
mech.initialize_led(LED_MID_O)
mech.initialize_led(LED_NEAR_O)

ON = 1
OFF = 0

SPKR = 12

mech.initialize_speaker(SPKR)

LOW_FREQ = 300

TRIG = 22
ECHO = 27

TRIG_O = 10
ECHO_O = 18

mech.initialize_ranger(TRIG, ECHO)
mech.initialize_ranger(TRIG_O, ECHO_O)


while True:
    distance = mech.get_distance(TRIG, ECHO)
    if distance != None:
        if distance > 15:
            mech.play_speaker(SPKR, OFF, 0)
        else:
            mech.play_speaker(SPKR, ON, 300)
    else:
        print("it's none")
"""
while True:
    distance = mech.get_distance(TRIG_O, ECHO_O)
    if distance != None:
        if distance > 15:
            mech.play_speaker(SPKR, OFF, 0)
        else:
            mech.play_speaker(SPKR, ON, 300)
    else:
        print("it's none")
"""
"""
for i in range(3):
    mech.set_led(LED_FAR, ON)
    time.sleep(1.5)
    mech.play_speaker(SPKR, ON, 300)
    time.sleep(1.5)
    mech.play_speaker(SPKR, OFF, 300)
    mech.set_led(LED_FAR, OFF)

    mech.set_led(LED_MID, ON)
    time.sleep(1.5)
    mech.set_led(LED_FAR, OFF)

    mech.set_led(LED_NEAR, ON)
    time.sleep(1.5)
    mech.set_led(LED_NEAR, OFF)

for i in range(3):
    mech.set_led(LED_FAR_O, ON)
    time.sleep(1.5)
    mech.play_speaker(SPKR, ON, 300)
    time.sleep(1.5)
    mech.play_speaker(SPKR, OFF, 300)
    mech.set_led(LED_FAR_O, OFF)

    mech.set_led(LED_MID_O, ON)
    time.sleep(1.5)
    mech.set_led(LED_FAR_O, OFF)

    mech.set_led(LED_NEAR_O, ON)
    time.sleep(1.5)
    mech.set_led(LED_NEAR_O, OFF)
"""
print("done")