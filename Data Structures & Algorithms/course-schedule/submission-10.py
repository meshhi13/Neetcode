class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(node: int) -> bool:
            neighbors, seen = adjMap[node][0], adjMap[node][1]
            return_val = True

            if seen == 1:
                return False

            if seen == 2:
                return True

            adjMap[node] = [neighbors, 1]

            for new_node in neighbors:
                if new_node == node:
                    return False

                if not dfs(new_node):  
                    return False

            adjMap[node][1] = 2

            return return_val


        adjMap = {}

        for i in range(numCourses):
            adjMap[i] = [[], 0]

        for i in prerequisites:
            adjMap[i[1]][0].append(i[0])

        for i in range(numCourses):
            if adjMap[i][1] == 2:
                continue

            if not dfs(i):
                return False

        return True