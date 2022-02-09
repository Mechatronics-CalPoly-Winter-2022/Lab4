import time
import serial
import matplotlib.pyplot as plt


def main():
    with serial.Serial('COM5', 115200) as ser:
        ser.reset_input_buffer()
        ser.reset_output_buffer()

        ser.write('\r\n'.encode('utf-8'))
        time.sleep(0.1)

        x_vals, y_vals = [], []
        while True:
            line = ser.readline().decode().strip()
            if line == 'end.':
                break
            if ',' in line:
                x, y = line.split(',')
                x_vals.append(float(x))
                y_vals.append(float(y))

        plt.plot(x_vals, y_vals, label='Step Response')
        plt.ylabel('Voltage (mV)')
        plt.ylim(bottom=0, top=3.3)
        plt.xlabel('Time (ms)')
        plt.margins(x=0, y=0)
        plt.show()


if __name__ == '__main__':
    main()
