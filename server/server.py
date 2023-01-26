# -*- coding: utf-8 -*-
import socket
import configparser
import os
from read_sensor_data import SENSOR

global conn

def run():	# Update Roll, Pitch and Yaw
    global conn
    read_data = SENSOR()
    seq_num = 0
    while True:
        data = read_data.read_data(seq_num)
        conn.sendall(data)
        seq_num += 1

    conn.close()

def socket_connection(config):
    global conn
    HOST = config['SOCKET']['host']
    PORT = int(config['SOCKET']['port'])

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen()

    conn, addr = server_socket.accept()

    print('Connected by', addr)


if __name__ == '__main__':
    global conn
    basepath = os.path.dirname(os.path.realpath(__file__))
    config = configparser.ConfigParser()
    config.read(basepath + '/config/config.ini')

    socket_connection(config)
    run()
    conn.close()
