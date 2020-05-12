# [435. Non-overalapping Interval](https://leetcode.com/problems/non-overlapping-intervals/)

## Python


```python
    class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        if len(intervals) == 1:
            return 0
        
        intervals.sort(key = lambda x:x[1])
        remove = 0
        end = intervals[0][0]
        
        for interval in intervals:
            if interval[0] < end:
                remove += 1
            else:
                end = interval[1]
                
                
        return remove
```
