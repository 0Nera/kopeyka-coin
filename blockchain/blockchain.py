from blockchain import block
from blockchain import config
from blockchain import pow

import time

blockchain = [
    block.block(
        time.time(), 
        {
            'message': 'Hello blockchain world!'
        },
        0,
        config.BLOCK_DIFF_MIN,
        '0'
    )
]



def get_blocks_count():
    return len(blockchain)



def get_last_block():
    return blockchain[-1].get_json()


