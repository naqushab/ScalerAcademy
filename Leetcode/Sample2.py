def solve(nums, k):
    mod =[0]*k
    count = 0
    n = len(nums)
    # populate mod array
    for i in range(n):
        mod[nums[i]%k] += 1
    count += mod[0]*(mod[0]-1)//2 # permutation
    
    for i in range(1, k):
        count += mod[0]*mod[i] # calculate permutation of each number with 0
    
    # need to take care of rest of cases
    for i in range(k):
        for j in range(i+1, k):
            if not mod[i] and not mod[j] and (i+1) * (j+1) == k:
                count += 1
    return count
    
print(solve(nums=[3, 2, 1], k=6))
print(solve(nums=[1, 15, 19, 2, 9, 6, 10, 12], k=3))