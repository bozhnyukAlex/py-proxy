import socket
import threading

from proxy import handle_connection

HOST = '127.0.0.1'
PORT = 8888
BUFF = 8192


def run_proxy():
    print('Proxy run\n')
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((HOST, PORT))
    sock.listen()

    while True:
        client_sock, addr = sock.accept()
        print(f'Socket accepted connection from {addr[0]}:{addr[1]}')
        threading.Thread(
            target=handle_connection,
            args=(client_sock,)
        ).start()


if __name__ == '__main__':
    run_proxy()
