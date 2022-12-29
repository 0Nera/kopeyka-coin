import os
import sys
import time
import socket
import threading
import json
import signal
import logging
from blockchain.blockchain import get_blocks_count, get_last_block

def handle_connection(sock, addr, pid):
    data = sock.recv(1024)
    try:
        data = json.loads(data.decode())
        
        if data['action'] == 'status':
            sock.send(
                str(json.dumps({
                    'status': 200,
                    'message': "I'm OK",
                    'blocks': get_blocks_count()
                })).encode()
            )
        elif data['action'] == 'exit':
            sock.send(
                str(json.dumps({
                    'status': 200,
                    'message': "OK"
                })).encode()
            )
            logging.error(f"{addr}[EXIT]")
            os.kill(pid, signal.SIGTERM)
        elif data['action'] == 'lastblock':
            sock.send(
                str(json.dumps({
                    'status': 200,
                    'data': get_last_block()
                })).encode()
            )
            logging.info(f"{addr}[lastblock]")
        elif data['action'] == 'get_user':
            data['key']
            sock.send(
                str(json.dumps({
                    'status': 200,
                    'data': "Hi!",
                })).encode()
            )
            logging.info(f"{addr}[lastblock]")
        else:
            logging.error(f"{addr}[{data['action']}, not found]")
            sock.send(
                str(json.dumps({
                    'status': 404,
                    'message': f"{data['action']}, not found"
                })).encode()
            )

    except Exception as E:
        logging.error(f"{addr}[{E}]")
        sock.send(
                str(
                    json.dumps(
                        {
                            'status': 500,
                            'message': str(E)
                        }
                    )
                ).encode()
            )
    sock.close()
    logging.info(f"{addr[0]}:{addr[1]} - exit")
      


def server_tcp(HOST='localhost', PORT=5000):
    print(f"{HOST}:{PORT} TCP server process on {os.getpid()} PID")
    pid = os.getpid()
    
    logging.basicConfig(filename='server_tcp.log', encoding='utf-8', level=logging.DEBUG)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serv_sock:
        serv_sock.bind((HOST, PORT))
        serv_sock.listen(0)
        
        while True:
            logging.info("Waiting for connection... ")
            sock, addr = serv_sock.accept()

            logging.info(f"{addr[0]}:{addr[1]} - connected")
            t = threading.Thread(target=handle_connection, args=(sock, addr, pid))
            t.start()
