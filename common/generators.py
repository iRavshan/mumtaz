import string
import random

def order_key_generator(length=6):
    chars = string.ascii_uppercase + string.digits
    return 'o'+''.join(random.choice(chars) for _ in range(length))

def customer_key_generator(length=6):
    chars = string.ascii_uppercase + string.digits
    return 'cu'+''.join(random.choice(chars) for _ in range(length))

def courier_key_generator(length=6):
    chars = string.ascii_uppercase + string.digits
    return 'co'+''.join(random.choice(chars) for _ in range(length))