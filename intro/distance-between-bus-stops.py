class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:

        start,destination = min(start,destination),max(start,destination)
        n = len(distance)
        distance.extend(distance)
        return min(sum(distance[start:destination]),sum(distance[destination:n+start]))
        