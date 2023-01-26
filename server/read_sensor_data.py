# -*- coding: utf-8 -*-
import json
import datetime
import pytz
import time
from sensor import SER

class SENSOR():
    def __init__(self):
        self.ser = SER()

    def read_data(self, seq):	# Update Roll, Pitch and Yaw
        data = self.ser.get(1)
        if len(data[0]) == 9:	# angles
            cur_date = datetime.datetime.now(pytz.timezone('Asia/Seoul'))
            cus_s = str(int(time.mktime(cur_date.timetuple())))
            cur_time = cus_s + '.' + cur_date.strftime("%f")

            data = {
                "filedKeys": {
                    'acc_x': float(data[0][0]),
                    'acc_y': float(data[0][1]),
                    'acc_z': float(data[0][2]),
                    'gyr_x': float(data[0][3]),
                    'gyr_y': float(data[0][4]),
                    'gyr_z': float(data[0][5]),
                    'ang_x': float(data[0][6]),  # roll, phi   (x축 회전각)
                    'ang_y': float(data[0][7]),  # pitch, theta(y축 호전각)
                    'ang_z': float(data[0][8]),
                    'seq': seq
                }
            }
            data = json.dumps(data).encode('utf-8')
            print('data : ', data)
            return data
        else:
            pass

if __name__ == '__main__':
    # test = SENSOR()
    # test.read_data()
    pass
