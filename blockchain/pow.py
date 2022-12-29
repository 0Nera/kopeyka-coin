import time
import hashlib


def pow_valid(last_hash, hash, pow, difficult=5):
    new_hash = hashlib.sha256(f"{last_hash}{pow}".encode('utf-8')).hexdigest()

    if hash != new_hash:
        return False
    elif new_hash[:difficult] != '0' * difficult:
        return False
    
    return True


def pow_worker(last_hash, difficult=5):
    new_hash = hashlib.sha256(str(last_hash).encode('utf-8')).hexdigest()
    pow = 0

    while pow_valid(last_hash, new_hash, pow, difficult):
        new_hash = hashlib.sha256(f"{last_hash}{pow}".encode('utf-8')).hexdigest()
        pow += 1
    
    return [new_hash, pow]


if __name__ == '__main__':
    _start = time.time()
    x = pow_worker(hashlib.sha256('123'.encode('utf-8')).hexdigest(), 5)
    _end = time.time() - _start
    print(f"POW: {x[1]} за {_end} секунд, хэш: {x[0]}")