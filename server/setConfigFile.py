import configparser
import os
import argparse

def config_generator(args):
    config = configparser.ConfigParser()
    filename = 'config.ini'

    basepath = os.path.dirname(os.path.realpath(__file__)) + '/config/'
    init_file = open(basepath+filename, 'w')
    init_file.close()

    config['SOCKET'] = {}
    config['SOCKET']['host'] = args.ip
    config['SOCKET']['port'] = args.port

    with open(basepath+filename, 'w', encoding='utf-8') as configfile:
        config.write(configfile)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Set Socket Infomation(host, port)')

    parser.add_argument('--ip', type=str)
    parser.add_argument('--port', type=str)

    args = parser.parse_args()

    config_generator(args)
