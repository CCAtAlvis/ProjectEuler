import time
start_time = time.time()

i = 0
permu = 0

def comb(io):
    global permu

    if len(io) == 2:
        if permu+1 == 1000000:
            return (True, str(io[1]) + str(io[0]))
        else:
            permu += 1
            return (False, 0)


    for x in io:
        temp = list()
        for i in io:
            temp.append(i)

        temp.remove(x)
        val = comb(temp)

        if val[0]:
            print(val, temp, x)
            return (True, str(x) + str(val[1]))

    return (False, 0)

val = comb(list(x for x in range(0,10)))

print(val)
print("--- %s seconds ---" % (time.time() - start_time))
