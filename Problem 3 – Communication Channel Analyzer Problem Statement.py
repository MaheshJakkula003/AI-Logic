def longest_unique(s):
    seen = set()
    left = 0
    max_len = 0

    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        seen.add(s[right])
        max_len = max(max_len, right - left + 1)

    return max_len



print(longest_unique("abcabcbb"))
#Hidden Tests
print("Testcase1:",longest_unique("a"))          
print("Testcase2:",longest_unique("aaaaaa"))     
print("Testcase3:",longest_unique("abcdef"))     
print("Testcase4:",longest_unique("aa"))         
print("Testcase5:",longest_unique("abca"))       
