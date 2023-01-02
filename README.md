# FFXLightningDodger
Automatic lightning dodger for Final Fantasy X using an Light Dependent Resistor (LDR) with a Raspberry Pico and CircuitPython


First install Circuit Python on your Pico: https://circuitpython.org/board/raspberry_pi_pico/


Download the libraries package: https://circuitpython.org/libraries


Copy the library 'adafruit_hid' to the /lib/ folder on the pico.

Copy the files boot.py and code.py to the root of the Pico.


Connect a Light Dependent Resistor to Analogue pin A2 on the board with a 10k resistor.
Point the LDR at your screen, in my case i'm using a steamdeck.

The onboard LED will light up when it detects lightning and stay lit when it's dodged 200 times.

![IMG_3630](https://user-images.githubusercontent.com/74387709/210271941-3d383b7f-efab-4916-810f-06ed3ab40ba6.jpeg)
