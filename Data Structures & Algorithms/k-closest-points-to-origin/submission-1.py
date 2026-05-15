class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = [round(math.sqrt(n[0]**2 + n[1]**2), 5) for n in points]

        mapper = {}
        for i in range(len(points)):
            mapper[distances[i]] = mapper.get(distances[i], [])
            mapper[distances[i]].append(points[i])
        heapq.heapify(distances)
        result = [] 

        for i in range(k):
            current_dis = heapq.heappop(distances)
            result.append(mapper[current_dis][0])
            mapper[current_dis].pop(0)
             
        return result