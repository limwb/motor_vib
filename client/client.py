# -*- coding: utf-8 -*-
import socket
import configparser
import os
from read_sensor_data import SENSOR

global client_socket

def run():	# Update Roll, Pitch and Yaw
    global client_socket
    read_data = SENSOR()
    while True:
        data = read_data.read_data()
        client_socket.sendall(data)

def socket_connection(config):
    global client_socket
    HOST = config['SOCKET']['host']
    PORT = int(config['SOCKET']['port'])

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

if __name__ == '__main__':
    basepath = os.path.dirname(os.path.realpath(__file__))
    config = configparser.ConfigParser()
    config.read(basepath + '/config/config.ini')

    socket_connection(config)
    run()
