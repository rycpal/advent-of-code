# Day 25: Combo Breaker
# <ryc> 2021

def search_loop(base):
    key = 1
    loop = 0
    while key != base:
        key *= 7
        key %= 20201227
        loop += 1
    return loop

def search_key(base, loop):
    key = 1
    for _ in range(loop):
        key *= base
        key %= 20201227
    return key

def encryption_key():
    card_key = 15335876
    door_key = 15086442
#    card_key = 5764801
#    door_key = 17807724
    card_loop = search_loop(card_key)
    print(card_loop)
    door_loop = search_loop(door_key)
    print(door_loop)
    card_encryption = search_key(card_key, door_loop)
    door_encryption = search_key(door_key, card_loop)
    return card_encryption, door_encryption

if __name__ == '__main__':
    print('\n25: Combo Breaker')
    print('\nencryption key:',encryption_key())
