import heapq

class Solution(object):
    def minCost(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        #  1. 그래프 구성 (정방향, 역방향 모두 저장)
        graph = [[] for _ in range(n)]
        rev_graph = [[] for _  in range(n)]
        for u, v, w in edges:
            graph[u].append((v, w))
            rev_graph[v].append((u, w))

        # 2. 거리 저장 (node, used_mask)
        distances = {}

        queue = [(0, 0, 0)]
        distances[(0, 0)] = 0

        while queue:
            curr_dist, u, mask = heapq.heappop(queue)

            if curr_dist > distances.get((u, mask), float('inf')):
                continue

            if u == n-1:
                return curr_dist
            
            for v, w in graph[u]:
                if curr_dist + w < distances.get((v, mask), float('inf')):
                    distances[(v, mask)] = curr_dist + w
                    heapq.heappush(queue, (curr_dist + w, v, mask))

            if not (mask & (1 << u)):
                new_mask = mask | (1 << u)
                for v, w in rev_graph[u]:
                    rev_cost = curr_dist + (2 * w)
                    if rev_cost < distances.get((v, new_mask), float('inf')):
                        distances[(v, new_mask)] = rev_cost
                        heapq.heappush(queue, (rev_cost, v, new_mask))

        return -1