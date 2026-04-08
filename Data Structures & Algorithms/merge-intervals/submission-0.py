class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x : x[0])
        merged = [intervals[0]]

        for i in range(1, len(intervals)):
            current_interval = intervals[i]
            recent_merged = merged[-1]

            if (current_interval[0] <= recent_merged[1]):
                recent_merged[1] = max(recent_merged[1], current_interval[1])
            else:
                merged.append(current_interval)
        
        return merged

