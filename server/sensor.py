import time
import serial

class SER:
    def __init__(self):
        self.port = '/dev/ttyS0'
        self.baud = 115200
        self._ser_data_list = []
        try:
            self._ser = serial.Serial(self.port, self.baud)
            self._ser.flushInput()
            self._ser.flushOutput()

            self._ser.write(b'sp=' + str(20).encode('ascii') + b'\r\n')
            time.sleep(0.03)
            self._ser.write(b'ss=' + str(7).encode('ascii') + b'\r\n')
            time.sleep(0.03)

        except Exception as e:
            print('serial error : ', e)

    def set_sensor20(self, sp=20):
        try:
            self._ser.write(b'sp=' + str(sp).encode('ascii') + b'\r\n')
            time.sleep(0.03)
        except Exception as e:
            print('set sensor error(sp-20) : ', e)

    def set_sensor7(self, ss=7):
        try:
            self._ser.write(b'ss=' + str(ss).encode('ascii') + b'\r\n')
            time.sleep(0.03)
        except Exception as e:
            print('set sensor error(sp-7) : ', e)

    def get(self, interval, count=2):
        if count == 0:
            self._ser_data_list.clear()
            return self._ser_data_list

        global pid

        while True:
            s = 0
            c = 0
            pre_c = 0
            record = []

            self._ser_data_list.clear()
            self._ser.flushInput()
            self._ser.flushOutput()

            try:
                while True:
                    c = self._ser.read(1)

                    if s == 0:
                        if c == b'\r':
                            pre_c = c
                        elif pre_c == b'\r' and c == b'\n':
                            s = 1
                        continue
                    elif s == 1:
                        if c == b'\r':
                            pre_c = c
                            continue
                        elif pre_c == b'\r' and c == b'\n':
                            s = 2
                        else:
                            record.append(c.decode('ascii'))

                    if s == 2:
                        values = ''.join(str(e) for e in record)
                        items = values.split()

                        record = []
                        s = 1

                        if len(items) >= 3:  # acc : 가속도[g] : 9.8m/s^2, gyr : 각속도, ang : 각도
                            self._ser_data_list.append(items)

                            count -= 1
                            if count <= 0:
                                return self._ser_data_list

            except Exception as e:
                print('data read error : ', e)