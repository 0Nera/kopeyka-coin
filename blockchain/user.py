class user:
    def __init__(self) -> None:
        self.__balance = 0
        
        self.__timestamp = 0
        self.__timestamp_last = 0

        self.__public_key = None
        self.__private_key = None

        self.__public_key_hash = None
        self.__private_key_hash = None

        self.__work_hash = None
