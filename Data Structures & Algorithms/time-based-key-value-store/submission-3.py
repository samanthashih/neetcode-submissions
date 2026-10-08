import bisect

class TimeMap:

    def __init__(self):
        self.values = defaultdict(dict)
        self.times = defaultdict(list[int])
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.insertValue(self.values[key], timestamp, value)
        self.insertTime(self.times[key], timestamp)
        return
    
    def insertValue(self, values: dict, time: int, val: str):
        values[time] = val
    
    def insertTime(self, l: list, time: int):
        l.append(time)
        l.sort()

    def get(self, key: str, timestamp: int) -> str:
        if key in self.values:
            if timestamp in self.values[key]:
                return self.values[key][timestamp]
            else:
                timestamp_prev = self.getNearestPrevTime(self.times[key], timestamp)
                if timestamp_prev is not -1: 
                    return self.values[key][timestamp_prev]
                else:
                    return ""
        else:
            return ""
    
    def getNearestPrevTime(self, l: list, time: int) -> int:
        idx = bisect.bisect_left(l, time)
        if idx > 0:
            idx -= 1

        nearestTime = l[idx]
        if time > nearestTime:
            return nearestTime
        else:
            return -1


# values = dict():
# alice: {1: "happy", 3: "sad"}
        
# times = dict()
# alice: [1,3] -> binary search for 2, return 1

# timeMap = TimeMap()
# timeMap.set("alice", "happy", 1)
# timeMap.set("alice", "sad", 3)
# print(timeMap.values)
# print(timeMap.times)
# print(timeMap.get("alice", 2))
