import time
start_time = time.time()

max_len = 0
max_num = 0

for i in range(1, 1000):
    rems = list()
    rem = 1
    while True:
        rem = rem%i
        if rem in rems:
            break
        else:
            rems.append(rem)
        rem *= 10

    if len(rems) > max_len:
        max_len = len(rems)
        max_num = i

    print(max_len, max_num)

print(max_num)
print("--- %s seconds ---" % (time.time() - start_time))
