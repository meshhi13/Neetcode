class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(node: int) -> bool:
            neighbors, seen = adjMap[node][0], adjMap[node][1]

            if seen == 1:
                return False

            if seen == 2:
                return True

            adjMap[node] = [neighbors, 1]

            for new_node in neighbors:
                if not dfs(new_node):  
                    return False

            adjMap[node][1] = 2

            return True

        adjMap = {i:[[], 0] for i in range(numCourses)}

        for i in prerequisites:
            adjMap[i[1]][0].append(i[0])

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True