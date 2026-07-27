class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {course: [[], -1, -1] for course in range(numCourses)}
        
        cycle = False

        for requisite in prerequisites:
            graph[requisite[1]][0].append(requisite[0])

        current_time = 0

        def dfs(node):
            nonlocal current_time, cycle
            neighbors, start, finish = graph[node]

            if finish != -1:
                return

            if start != -1:
                cycle = True
                return

            graph[node][1] = current_time
            current_time += 1

            for neighbor in neighbors:
                dfs(neighbor)

            graph[node][2] = current_time
            current_time += 1

        for course in range(numCourses):
            dfs(course)

        graph = sorted(graph, key=lambda x: -graph[x][2])
        return graph if not cycle else []