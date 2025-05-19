class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        def help(i):
            return i[1]
        
        intervals.sort(key=help)
        count = 1
        i = 0
    
        for j in range(1, len(intervals)):
            if intervals[j][0] >= intervals[i][1]:
                count += 1
                i = j
        
        return len(intervals) - count

        