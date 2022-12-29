import time
import json
import hashlib


class block:
    def __init__(self, timestamp=time.time(), data=None, pow=0, difficult=5, prev_hash='0') -> None:
        self.__timestamp = timestamp
        self.__data = data
        self.__pow = 0
        self.__difficult = difficult
        self.__prev_hash = prev_hash
        self.__hash = None
        self.create_hash()
    
    def get_hash(self):
        return self.__hash
    
    def create_hash(self):
        data = str(self.__timestamp) + str(self.__data) + str(self.__prev_hash)
        self.__hash = hashlib.sha256(data.encode('utf-8')).hexdigest()
    
    def get_json(self):
        return json.dumps(
            {
                'timestamp': self.__timestamp,
                'data': self.__data,
                'pow': self.__pow,
                'diff': self.__difficult,
                'prev': self.__prev_hash,
                'hash': self.__hash
            }
        )
    

if __name__ == '__main__':
    b = block()
    print(b.get_json())