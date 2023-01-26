import socket
import json
import matplotlib.pyplot as plt
import configparser
import os

from matplotlib.animation import FuncAnimation
from dbconnection import MongoDB

global client_socket

def run(config):
    socket_connection(config)
    ### show data start
    # show_realtime_graph()

    # connection DB
    db = MongoDB()
    while True:
        data_to_dict = recv_data()
        print(data_to_dict)
        db.insert_data(data_to_dict)


def show_realtime_graph():
    fig, ax = plt.subplots()

    x = [0]
    y1 = [0]
    y2 = [0]
    y3 = [0]

    animation = FuncAnimation(fig, animate, fargs=(ax, x, y1, y2, y3), interval=1)
    plt.show()

def socket_connection(config):
    global client_socket
    HOST = config['SOCKET']['host']
    PORT = int(config['SOCKET']['port'])

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

def recv_data():
    global client_socket
    try:
        data = client_socket.recv(1024)
        data_to_str = data.decode('utf-8')
        data_to_dict = json.loads(data_to_str)

        return data_to_dict['filedKeys']
    except Exception as e:
        print(e)

def animate(i, ax, x, y1, y2, y3):
    x.append(x[-1] + 1)
    try:
        data_to_dict = recv_data()
        y_data_x = data_to_dict['acc_x']
        y_data_y = data_to_dict['acc_y']
        y_data_z = data_to_dict['acc_z']

    except Exception as e:
        print('data parsing error', e)
        y_data_x = 0.
        y_data_y = 0.
        y_data_z = 0.
    # print(data)
    y1.append(y_data_x)
    y2.append(y_data_y)
    y3.append(y_data_z)

    # lately data(100 EA)
    x = x[-100:]
    y1 = y1[-100:]
    y2 = y2[-100:]
    y3 = y3[-100:]

    ax.clear()

    # ax.set_xlim(0, 100)
    ax.set_ylim(-3, 3)

    ax.plot(x, y1, label='acc_x')
    ax.plot(x, y2, label='acc_y')
    ax.plot(x, y3, label='acc_z')

if __name__ == '__main__':
    basepath = os.path.dirname(os.path.realpath(__file__))
    config = configparser.ConfigParser()
    config.read(basepath + '/config/config.ini')

    run(config)

