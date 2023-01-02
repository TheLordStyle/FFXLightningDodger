import usb_hid

# These are the default devices, so you don't need to write
# this explicitly if the default is what you want.
usb_hid.enable(
    (usb_hid.Device.KEYBOARD,
     usb_hid.Device.MOUSE,
     USB_hid.Device.CONSUMER_CONTROL)
)

usb_hid.enable((usb_hid.Device.KEYBOARD,))   # Enable just KEYBOARD.

usb_hid.disable()       # Disable all HID devices.

usb_hid.enable(())      # Another way to disable all the devices.