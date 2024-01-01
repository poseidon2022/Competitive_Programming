class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        #maximum  of the two processors total time will be the min time
        #larger time tasks to lower available processors 
        tasks.sort(reverse = True)
        processorTime.sort()
        ans = 0
        i = 0
        print(tasks, processorTime)
        for idx, val in enumerate(processorTime):
            ans = max(ans, val + tasks[i])
            i+=4
        
        return ans
        