class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets = sorted(tickets, key=lambda x:x[1])
        
        flight_map = {ticket[0]: [] for ticket in tickets}

        for ticket in tickets:
            flight_map[ticket[0]].append(ticket[1])

        path = ["JFK"]

        def dfs(start):
            if len(path) == len(tickets) + 1:
                return True

            if start not in flight_map:
                return False

            temp_array = list(flight_map[start])
            for index, neighbor in enumerate(temp_array):
                path.append(neighbor)
                flight_map[start].pop(index)

                if dfs(neighbor):
                    return True

                path.pop()
                flight_map[start].insert(index, neighbor)

            return False


        dfs("JFK")
        return path
