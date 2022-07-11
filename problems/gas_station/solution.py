class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_destinations = len(gas)
        start_point = 0
        while start_point < total_destinations:
            gas_consumed = 0
            trip_point = 0
            while trip_point < total_destinations:
                current_point = (start_point + trip_point) % total_destinations
                gas_consumed += gas[current_point] - cost[current_point]
                if gas_consumed < 0:
                    break
                trip_point += 1
            if trip_point == total_destinations:
                return start_point
            start_point += trip_point + 1
        return -1