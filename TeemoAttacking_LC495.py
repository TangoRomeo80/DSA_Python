class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        # 1. find the total time
        # 2. return the total time
        total_time = 0
        for i in range(len(timeSeries) - 1):
            if timeSeries[i] + duration <= timeSeries[i + 1]:
                total_time += duration
            else:
                total_time += timeSeries[i + 1] - timeSeries[i]
        return total_time + duration if len(timeSeries) > 0 else 0