import serial


def read():
    """ Read code """
    pass


if __name__ == '__main__':
    with serial.Serial('/dev/ttyACM0', 115200, timeout=2,
                       parity=serial.PARITY_EVEN, rtscts=1, bytesize=8) as ser:
        while(True):
            print(ser.readline())
    # device = evdev.InputDevice('/dev/input/event22')
    # print(device)
    # for event in device.read_loop():
    #     print(event)
