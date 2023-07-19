from Crypto.Random import random

def generate_random_sequenced_array(min_num=0, max_num=2048):
    array = [a for a in range(min_num, max_num)]
    array = array_randomizer(array)
    return array

def generate_random_array(size=2048, min_num=0, max_num=2048):
    array = []
    for _ in range(size):
        array.append(random.randint(min_num, max_num))
    return array

def array_randomizer(array=None):
    if array is None:
        array = [a for a in range(0, 1024)]
    random.shuffle(array)
    return array
