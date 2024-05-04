class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key = lambda x: x[0] - x[1])
        n = len(costs)//2
        mincost = 0
        for i in range(len(costs)):
            if i < n:
                mincost += costs[i][0]
            else:
                mincost += costs[i][1]
        return mincost