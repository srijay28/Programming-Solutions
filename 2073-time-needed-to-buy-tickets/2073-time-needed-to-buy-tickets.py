class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        l = len(tickets)
        t = 0
        while True:
            for i in range(len(tickets)):
                if tickets[i] == 0: continue
                tickets[i] -= 1
                t += 1
                if i == k and tickets[i] == 0:
                    break
            if tickets[k] == 0:
                return t