from multiprocessing import Process, Pipe
from bots.main import miner_bot
from server.server_tcp import server_tcp
from config import HOST, PORT


if __name__ == '__main__':
    pipe_output, pipe_input = Pipe()

    
    server_tcp_process = Process(target=server_tcp, args=(HOST, PORT,))
    server_tcp_process.start()

    
    miner_bot_process = Process(target=miner_bot, args=(0,))
    miner_bot_process.start()