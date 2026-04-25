def time_slots(ranges):
    ranges.sort()              # Applying sorting
    x = []
    for start, end in ranges:
        if not x or x[-1][1] < start:
            x.append([start, end])        # non-overlapping range
        else:
            x[-1][1] = max(x[-1][1], end)  # merging
    return x


sample = [[1,3],[2,6],[8,10],[15,18]] #sample
ranges1 = [[5,19]] #Testcase1 
ranges2 = [[1,10],[2,8],[3,7]] #Testcase2
ranges3 = [[1,2],[4,5],[7,8]]            #Testcase3 
ranges4 = [[8,10],[1,3],[15,18],[2,6]]    #Testcase4
ranges5 = [[1,5],[5,7],[7,10]]           #Testcase5

print("Sample:", time_slots(sample))
print("Testcase1:", time_slots(ranges1))
print("Testcase2:", time_slots(ranges2))
print("Testcase3:", time_slots(ranges3))
print("Testcase4:", time_slots(ranges4))
print("Testcase5:", time_slots(ranges5))
