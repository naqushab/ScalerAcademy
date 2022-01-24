class TimeMap:

    def __init__(self):
        self.tm = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.tm[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.tm:
            return ""
        times = self.tm[key]
        if timestamp < times[0][0]:
            return ""
        else:
            l, r = 0, len(times)-1
            while l <= r:
                m = (l+r)//2
                mid_time = times[m][0]
                if mid_time == timestamp:
                    return times[m][1]
                elif mid_time > timestamp:
                    r = m - 1
                else:
                    l = m + 1
            return times[l-1][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)