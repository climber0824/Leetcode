class Solution:
    def minExtraChar(self, s: str, wordDict: List[str]) -> int:
        """
        https://leetcode.com/problems/extra-characters-in-a-string/solutions/3568582/2-approach-dp-memoization-trie-approach-detailed-explanation/
        The value of dp[i] represents the minimum number of extra characters left over 
        if we break up the substring s[i..n-1] optimally.
        leetscode
        [0 1 2 3 4 0 0 0 0]
        i = 4, j = 0
           |
        |
        l not in dic
        le not in dic
        lee not in dic
        leet in dic -> remove -> 0 left
        s not in dic
        sc not in dic
        sco not in dic
        scod not in dic
        scode -> code in dic -> s left -> =1
        """
        word_set = set(wordDict)
        n = len(s)
        dp = [0] * (n + 1)
        for i in range(1, n+1):
            dp[i] = dp[i-1] + 1
            for j in range(i-1, -1, -1):
                substring = s[j:i]
                if substring in word_set:
                    dp[i] = min(dp[i], dp[j])        
        return dp[-1]
