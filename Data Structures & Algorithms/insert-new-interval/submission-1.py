class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        import bisect
        
        index = bisect.bisect_left(intervals, newInterval)
        intervals.insert(index, newInterval)

        res = [intervals[0]]

        for i in range(1, len(intervals)):
            current = intervals[i]
            merged = res[-1]

            if current[0] <= merged[1]:
                merged[1] = max(merged[1], current[1])
            else:
                res.append(current)

        return res