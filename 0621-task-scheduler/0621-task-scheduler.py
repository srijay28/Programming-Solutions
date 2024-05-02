class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        d = Counter(tasks)
        freq = [-s for s in d.values()]
        heapq.heapify(freq)

        queue = []
        t = 0
        while freq or queue:
            if freq:
                el = heapq.heappop(freq)
                t += 1
                el += 1
                if el < 0:
                    queue.append([el,t+n]) #t+n is the time AFTER which el is ready
            else:
                t = queue[0][1]
            
            if queue and queue[0][1] == t: #it is time to bring out the element in the queue
                element = queue.pop(0)
                heapq.heappush(freq,element[0])
        return t

        