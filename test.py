import time

time_ms = lambda: round(time.time() * 1000)

def lspeed(iters=2, list_size=10):
    print("start testing with {0} iterations and {1} list size".format(iters, list_size))
    arr = []
    beginning = time_ms()
    for i in range(iters):
        l = [x for x in range(list_size)]
        # arr.append(l)
        # print(arr)
    end = time_ms()
    print("Finished in {0}ms".format(end - beginning))

lspeed(100000, 100)
# lspeed()
# print(time_ms())