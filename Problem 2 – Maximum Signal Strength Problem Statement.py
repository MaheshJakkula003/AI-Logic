def max_sum_k(nums, k):
    # Initial window sum
    window_sum = sum(nums[:k])
    max_sum = window_sum

    # Slide the window
    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i-k]   # add new, remove old
        max_sum = max(max_sum, window_sum)

    return max_sum

print("sample:", max_sum_k([2,1,5,1,3,2], 6))
# Testcases
print("Testcase1:", max_sum_k([4,2,7,1,9], 1))       
print("Testcase2:", max_sum_k([1,2,3,4], 2))
print("Testcase3:", max_sum_k([-8,-3,-6,-2,-5], 2))  
print("Testcase4:", max_sum_k([1,2,3,4,5], 3))       
print("Testcase5:", max_sum_k([4,-1,-2,1,-5,4], 3))  
