class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = { i:[] for i in range(n)}

        visited = set()

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(node):

            for nei in adj[node]:
                if nei not in visited:
                    visited.add(nei)
                    dfs(nei)
                
            return 
            
        res = 0
        for node in range(n):
            if node not in visited:
                visited.add(node)
                dfs(node)
                res+=1
        return res
