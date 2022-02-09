import pyb
import utime
from task_share import Queue

if __name__ == '__main__':

    pinPC1 = pyb.Pin('PC1', pyb.Pin.OUT_PP)
    pinPC0 = pyb.Pin('PC0', pyb.Pin.IN)
    adc = pyb.ADC(pinPC0)
    q = Queue('H', 1000, name='q')
    tim1 = pyb.Timer(1)

    while True:
        input('Enter to start...')

        def adc_isr(tim1):
            if not q.full():
                q.put(adc.read())
            else:
                tim1.callback(None)
                pinPC1.low()

        tim1.init(freq=1000, callback=adc_isr)
        pinPC1.high()

        print('Starting loop')

        while pinPC1.value():
            utime.sleep_ms(1)

        print('Closing...')
        time_val = 1
        while q.any():
            print(f'{time_val},{round(q.get() / 4096 * 3.3, 2)}')
            time_val += 1
        print('end.')
