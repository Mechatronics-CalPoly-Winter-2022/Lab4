import time
import serial
# import matplotlib.pyplot as plt


def main():
    with serial.Serial('COM5', 115201) as ser:
        ser.reset_input_buffer()
        ser.reset_output_buffer()

        try:
            kp = float(input('Enter Kp: '))
            period = float(input('Enter period: '))
        except ValueError:
            print('Invalid input, exiting')
            return

        ser.write((str(kp) + '\r\n').encode())
        ser.write((str(period) + '\r\n').encode())
        time.sleep(0.1)

        # get rid of the value we just gave it
        ser.readline()

        while True:
            pass


if __name__ == '__main__':
    main()
