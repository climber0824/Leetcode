class Solution:
    MOD = 10 ** 9 + 7

    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        n = len(locations)
        MOD = 10**9+7
        dp = [[None] * (fuel + 1) for _ in range(n)]
        
        return self.helper(locations, start, finish, fuel, dp)

    def helper(self, locations, city, end, remainFuel, dp):
        if remainFuel < 0:
            return 0
        if dp[city][remainFuel] is not None:
            return dp[city][remainFuel]
        ans = 1 if city == end else 0

        for next_city in range(len(locations)):
            if next_city != city and remainFuel >= abs(locations[next_city] - locations[city]):
                ans = (ans + self.helper(locations, next_city, end, remainFuel - abs(locations[next_city] - locations[city]), dp)) % self.MOD
        dp[city][remainFuel] = ans
        
        return ans
