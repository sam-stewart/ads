import time
from queue import ArrayQueue
from shopper import Shopper
import random
import timeit
from checkout import Checkout
import os

LOAD_VALUE_MIN = 15
LOAD_VALUE_MAX = 20
QUEUES = 10
CHECKOUTS = 10
SHOPPERS = 1000

def simulate():
    checkouts = {}
    for i in range(CHECKOUTS):
        checkouts[i] = { 'queue' : ArrayQueue(),
                        'shopper' : None }
    checkouts = [Checkout() for i in range(CHECKOUTS)]
    queues = [ArrayQueue() for i in range(QUEUES)]
    shoppers = [Shopper(random.randint(LOAD_VALUE_MIN, LOAD_VALUE_MAX)) for i in range(SHOPPERS)]
    shoppers_left = SHOPPERS
    last_time = time.time()

    while True:
        c_time = time.time()

        if ((c_time - last_time) >= 0.5):
            queue = queues[random.randint(0, len(queues)-1)]
            shopper = shoppers.pop()
            shoppers_left -= 1
            queue.enqueue(shopper)
            last_time = c_time
            visualise(queues, shoppers_left)

        for i in range(CHECKOUTS):
            checkout = checkouts[i]
            queue = queues[i]
            shopper = checkout.shopper
            if shopper == None:
                if(len(queue) != 0):
                    checkout.shopper = queues[i].dequeue()
                    checkout.shopper.started_checkout = c_time

            elif ((shopper.started_checkout + shopper.load_value) <= c_time):
                checkout.shopper = None;

def visualise(queues, shoppers_left,longest_queue=20,):
    os.system('clear')
    string = ''

    for i in range(len(queues)):
        q = queues[i]
        string += str(i) + '|'
        string += ' * ' * len(q) + '\n\n'

    print string
       
if __name__ == '__main__':
    timeit.timeit(simulate());

