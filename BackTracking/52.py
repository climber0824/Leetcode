"""
For each row: check if can place queen.
Queen can't not be placed in positive diagonal or negative diagonal or same col.
"""

class Solution:
    def totalNQueens(self, n: int) -> int:
        cols = set()
        positiveDiagonal, negtiveDiagonal = set(), set()
        res = 0

        def backTrack(r):
            if r == n:
                nonlocal res
                res += 1
                return res
            for c in range(n):
                if c in cols or (r+c) in positiveDiagonal or (r-c) in negtiveDiagonal:
                    continue
                cols.add(c)
                positiveDiagonal.add(r+c)
                negtiveDiagonal.add(r-c)
                backTrack(r+1)
                cols.remove(c)
                positiveDiagonal.remove(r+c)
                negtiveDiagonal.remove(r-c)
        
        backTrack(0)
        return res
