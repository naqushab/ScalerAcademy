class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        if n < 3:
            return False
        
        if arr[0] > arr[1]:
            return False
        
        monotonic_increasing = True
        monotonic_decreasing = False
        deflection_point = False
        
        for i in range(1, n):
            if arr[i-1] == arr[i]:
                return False
            elif arr[i-1] < arr[i]:
                if monotonic_increasing:
                    continue
                else:
                    return False
            else:
                if monotonic_increasing:
                    monotonic_increasing = False
                    if not deflection_point:
                        deflection_point = True
                        monotonic_decreasing = True
                    else:
                        return False
                if monotonic_decreasing:
                    continue
        return deflection_point