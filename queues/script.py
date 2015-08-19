import time
from queue import ArrayQueue, EmptyException
import random
import timeit
import os

DIVISOR = 25
LOAD_MIN =  2.0 / DIVISOR
LOAD_MAX = 6.0 / DIVISOR
SHOPPERS = 1000
QUEUE_RATE = 0.4 / DIVISOR
QUEUES = 10

def simulate(queue_func):
    queues = [ArrayQueue() for _ in range(QUEUES)]
    shoppers = [{'started_checkout':None,'load':random.uniform(LOAD_MIN, LOAD_MAX)} \
            for i in range(SHOPPERS)]

    last_time = 0
    last_render = 0
    queues_empty = True
    while len(shoppers) > 0 or not queues_empty:
        c_time = time.time()
        if (c_time - last_time) >= QUEUE_RATE and len(shoppers) > 0:
            queue_func(queues, shoppers)
            last_time = c_time

        queues_empty = True
        shortest_queue = queues[0]
        for q in queues:
            try:
                shopper = q.first()
                queues_empty = False
                if shopper.get('started_checkout') == None:
                    shopper['started_checkout'] = c_time
                elif (shopper['started_checkout'] + shopper['load']) <= c_time:
                    q.dequeue()
            except EmptyException:
                pass

        if(c_time - last_render > QUEUE_RATE):
            visualise(queues, len(shoppers))
            last_render = c_time

def random_enqueue(queues, shoppers):
    queue = queues[random.randint(0, len(queues)-1)]
    queue.enqueue(shoppers.pop())

def shortest_queue(queues, shoppers):
    shortest_queue = queues[0]
    for i in range(1,len(queues)):
        if len(queues[i]) < len(shortest_queue):
            shortest_queue = queues[i]
    shortest_queue.enqueue(shoppers.pop())

def visualise(queues, num_shoppers):
    os.system('clear')
    string = ''

    for i in range(len(queues)):
        q = queues[i]
        string += str(i) + '|'
        string += ' * ' * len(q) + '\n\n'

    print string
    print "Shoppers left: " + str(num_shoppers)

if __name__ == '__main__':
    timer = timeit.Timer(stmt='simulate(random_enqueue)', setup='from __main__ import simulate, \
            random_enqueue');
    random_choice = timer.repeat(repeat=2, number=1)

    timer = timeit.Timer(stmt='simulate(shortest_queue)', setup='from __main__ import simulate, \
            shortest_queue')

    shortest = timer.repeat(repeat=2, number=1)
    print random_choice
    print shortest

