"""
#https://www.geeksforgeeks.org/subset-sum-problem-dp-25/

Given a set of non-negative integers, and a value sum, determine if there is a subset of the given set with sum equal to given sum.
Example:
Input: set[] = {3, 34, 4, 12, 5, 2}, sum = 9
Output: True
There is a subset (4, 5) with sum 9.

Input: set[] = {3, 34, 4, 12, 5, 2}, sum = 30
Output: False
There is no subset that add up to 30.
"""

def sol(nums, sum):
    n = len(nums)
    dp = [[False] * (sum + 1) for _ in range(n + 1)]
    
    # initialize row_0 and col_0
    for i in range(n + 1):
        dp[i][0] = True
    for i in range(1, sum + 1):
        dp[0][i] = False
    
    for i in range(1, n + 1):
        for j in range(1, sum + 1):
            if j < nums[i-1]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = (dp[i-1][j] or dp[i-1][j-nums[i-1]])
                
    return dp[n][sum]



if __name__ == '__main__':
    set = [3, 34, 4, 12, 5, 2]
    sum = 30
    print(sol(set, sum))
