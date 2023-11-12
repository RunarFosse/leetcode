# Author: Runar Fosse
# Time complexity: O(n+m)
# Space complexity: O(n+m)

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        # Using BFS
        if source == target:
            return 0

        # Create graph
        stop_to_bus = {}
        bus_to_stops = []
        for bus, route in enumerate(routes):
            bus_to_stops.append(set())
            for stop in route:
                if stop not in stop_to_bus:
                    stop_to_bus[stop] = set()
                stop_to_bus[stop].add(bus)
                bus_to_stops[bus].add(stop)
        adjs = []
        for bus, route in enumerate(routes):
            adjs.append(set())
            for stop in route:
                adjs[bus].update(stop_to_bus[stop])

        # Then perform BFS
        visited = set()
        queue = deque()
        # Add all busses we can take from source
        for bus in stop_to_bus[source]:
            queue.append((bus, 1))

        while queue:
            bus, distance = queue.popleft()
            if target in bus_to_stops[bus]:
                return distance
            if bus in visited:
                continue
            visited.add(bus)

            for neighbour in adjs[bus]:
                if neighbour not in visited:
                    queue.append((neighbour, distance+1))
        
        return -1
        
# This can be decomposed into a graph problem, where a given node represents a bus, and 
# adjacency list represent other busses directly reachable by current bus.
# To translate between stops and busses we can use a hashmap and array.
# Then we can perform BFS and find the smallest number of busses needed to reach target.