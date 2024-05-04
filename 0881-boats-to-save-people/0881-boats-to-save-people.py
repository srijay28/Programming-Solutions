class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boats = 0
        l , r = 0 , len(people)-1
        while l <= r:
            boats += 1
            if people[l]+people[r] <= limit:
                l += 1
            r -=1 
        return boats