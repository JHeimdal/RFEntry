import serial
from serial.serialutil import SerialException
import sys

def read():
    """ Read code """
    pass


if __name__ == '__main__':
    try:
        ser = serial.Serial('/dev/ttyACM0', 115200, timeout=2,
                            parity=serial.PARITY_EVEN, rtscts=1, bytesize=8)
    except SerialException as err:
        print(err)
        sys.exit(9)

    while(True):
        val = ser.readline()
        if val:
            try:
                print(int(val))
            except ValueError:
                print("Do something")
            
    # device = evdev.InputDevice('/dev/input/event22')
    # print(device)
    # for event in device.read_loop():
    #     print(event)
