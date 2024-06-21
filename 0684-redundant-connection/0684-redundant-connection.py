class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        #use union-find and when the parents are same of two different nodes,
        #that means they are already connected and we are adding a cycle
        par = [i for i in range(len(edges))]
        rank = [i for i in range(len(edges))]

        def find(n1):
            res = n1
            while res != par[res]:
                par[res] = par[par[res]]
                res = par[res]
            return res
        
        def union(n1,n2):
            p1 , p2 = find(n1) , find(n2)
            
            if p1 == p2:
                return (n1,n2)
            if rank[p1] > rank[p2]:
                rank[p1] += rank[p2]
                par[p2] = p1
            else:
                rank[p2] += rank[p1]
                par[p1] = p2
            return 
        
        for i,j in edges:
            if union(i-1,j-1):
                return [i,j]