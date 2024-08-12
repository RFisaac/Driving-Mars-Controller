import machine
import usb_hid

# Set the USB mode to include HID
usb_hid.enable((usb_hid.HID_GAMEPAD,))
