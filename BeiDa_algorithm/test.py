from timeit import Timer
import random

for i in range(10000, 1000001, 20000):
    t = Timer(f"random.randrange({i}) in x", "from __main__ import random, x")
    x = list(range(i))
    list_time = t.timeit(number=1000)
    x = {j: None for j in range(i)}
    dict_time = t.timeit(number=1000)
    print(f'i: {i}\t\tlist_time: {list_time:.5f}\t\tdict_time: {dict_time:.5f}')
