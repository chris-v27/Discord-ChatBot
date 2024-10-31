import random

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password
def flip_coin():
    side = random.randint(1,2)
    if side == 1:
        return 'cara'
    elif side == 2: 
        return 'cruz'
