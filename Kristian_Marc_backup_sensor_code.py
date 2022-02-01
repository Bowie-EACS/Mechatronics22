import mechatronics as mech
import time





#hook up led to designated pin
LED_FAR = 10
LED_MID = 9
LED_NEAR = 11

#initialize led
mech.initialize_led(LED_FAR)
mech.initialize_led(LED_MID)
mech.initialize_led(LED_NEAR)

ON = 1
OFF = 0

#initialize speaker
SPKR = 17
mech.initialize_speaker(SPKR)

LOW_FREQ = 300

mech.set_led(LED_NEAR, ON)
time.sleep(1.5)

TRIG = 22
ECHO = 27
#pins for sonic sensor
TRIG2 = 14
ECHO2 = 15

#initialize sensors
mech.initialize_ranger(TRIG, ECHO)
mech.initialize_ranger(TRIG2, ECHO2)

#function to turn all lights on
def turn_all_led_on():
    mech.set_led(LED_NEAR, ON)
    mech.set_led(LED_MID, ON)
    mech.set_led(LED_FAR, ON)
turn_all_led_on()

##Function to get distance away from sensor and play sound/signal lights
def print_distance_then_wait():
    distance = mech.get_distance(TRIG, ECHO)
    while True:
        print ("The distance is", distance)
        if distance != None:
            if distance > 10:
                time.sleep(2)
                mech.play_speaker(SPKR, OFF, 0)
            elif (distance < 10) and (distance >= 5):
                time.sleep(0.1)
                mech.play_speaker(SPKR, ON, 200)
                mech.set_led(LED_NEAR, ON)
            elif (distance < 5):
                turn_all_led_on()
                time.sleep(1)


        
        
#function for second sensor
def sensor2():
    while True:
        distance2 = mech.get_distance(TRIG2, ECHO2)
        print ("This distance is", distance2)
        if distance2 != None:
            if distance2 > 10:
                time.sleep(2)
                mech.play_speaker(SPKR, OFF, 0)
                mech.set_led(LED_FAR, ON)
                mech.set_led(LED_MID, ON)
            elif (distance2 < 10) and (distance2 >= 5):
                time.sleep(0.1)
                mech.play_speaker(SPKR, ON, 200)
                mech.set_led(LED_NEAR, ON)
            elif (distance2 < 5):
                mech.play_speaker(SPKR, ON, 100)
                m(LED_MID, ON)
                time.sleep(1.5)

try:
    print_distance_then_wait()
except KeyboardInterrupt:
    mech.set_led(LED_FAR, OFF)
    mech.set_led(LED_MID, OFF)
    mech.set_led(LED_NEAR, OFF)
    mech.play_speaker(SPKR, OFF, 0)
    mech.cleanup()








