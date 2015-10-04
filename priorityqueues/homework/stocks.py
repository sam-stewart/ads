from priorityqueue import PriorityQueue
import random


""" A script representing one round of stock trading we assume each buyer and
seller is looking to buy or sell exactly 100 shares. """

buyers = [{"name": "Sam", "bought": 0},
          {"name": "Rickie", "bought": 0},
          {"name": "Matt", "bought": 0}]

sellers = [{"name": "Alex", "sold": 0},
           {"name": "Daniel", "sold": 0},
           {"name": "Thomas", "sold": 0}]

buy_orders, sell_orders = PriorityQueue(), PriorityQueue()

for e in buyers:
    buy_orders.add(random.randint(5, 100), e)

for e in sellers:
    sell_orders.add(random.randint(5, 100), e)

while len(buy_orders) != 0:
    buy = buy_orders.remove_min()
    if buy[0] < sell_orders.min()[0]:
        # add to a list for next round
        pass
    else:
        buy[1]["bought"] += 100
        sell_orders.remove_min()[1]["sold"] += 100

for e in buyers:
    print e["name"] + " bought " + str(e["bought"]) + " shares"

for e in sellers:
    print e["name"] + " sold " + str(e["sold"]) + " shares"
