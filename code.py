import time
import board
import analogio
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

kbd = Keyboard(usb_hid.devices)

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

lower_threshold =  15000
upper_threshold = 20000

sensor = analogio.AnalogIn(board.A2)

state_index = False
lightning_strikes=0

# Flash the onboard Led twice to show it's powered on
led.value = True
time.sleep(0.1)
led.value = False
time.sleep(0.1)
led.value = True
time.sleep(0.1)
led.value = False

while True:

    # The target amount of dodges
    if lightning_strikes > 200:
        led.value = True
    sensor_level = sensor.value
    
    if state_index is False:
        if sensor_level < lower_threshold:
            led.value = False
            state_index = True

    elif state_index is True:
        if sensor_level > upper_threshold:
            # Simulate a button press for the 'c' key
            kbd.press(Keycode.C)
            time.sleep(0.3)
            kbd.release(Keycode.C)
            led.value = True
            state_index = False
            lightning_strikes += 1
    print(sensor_level)