# Default - default value for the parameters


def shipping_cost(total_amount, discount=0, tax=0.06):
    return total_amount + (1-discount)+(1-tax)

# print(shipping_cost(500))
# print(shipping_cost(500,10,0)

import time

def count(start,end):
    for x in range(start,end+1):
        print(x)
        time.sleep(1)
    print('Done')
count(1,10)
