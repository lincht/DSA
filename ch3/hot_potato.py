import random
from linear_data_structure import Queue


def hot_potato(ls):
    """Hot Potato simulation that allows for a random counter."""
    
    q = Queue()
    for name in ls:
        q.enqueue(name)
    
    while q.size() > 1:
        counter = random.randrange(1, 21)
        for _ in range(counter):
            q.enqueue(q.dequeue())
        q.dequeue()
    
    return q.dequeue()


def main():
    print(hot_potato(['Bill', 'David', 'Susan', 'Jane', 'Kent', 'Brad']))


if __name__ == '__main__':
    main()