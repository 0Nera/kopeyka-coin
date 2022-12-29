import socket
import sys
import json
from blockchain.pow import pow_valid, pow_worker

HOST, PORT = "localhost", 5000

def send_message(data):
    print(f"Send:     {data}")

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))
    sock.sendall(bytes(json.dumps(data), "utf-8"))
    received = str(sock.recv(1024), "utf-8")
    sock.close()
    
    return received


def miner_bot(bot_id):
    print(f"Bot #{bot_id} mining process")

    #   -------  status
    msg = send_message({
        "action": "status"
    })
    print(f"Received: {msg}")

    #   -------  lastblock
    msg = send_message({
        "action": "lastblock"
    })
    if json.loads(msg)['status'] == 200:
        print(f"Received: {json.loads(msg)['data']}")

    #   -------  get_user
    msg = send_message({
        "action": "get_user"
    })
    if json.loads(msg)['status'] == 200:
        print(f"Received: {json.loads(msg)['data']}")

    #   -------  exit
    msg = send_message({
        "action": "exit"
    })
    print(f"Received: {msg}")


    print("End")