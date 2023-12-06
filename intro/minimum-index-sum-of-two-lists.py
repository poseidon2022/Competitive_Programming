class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:

        counter = defaultdict(int)
        index_sum = defaultdict(int)
        
        def counter_and_index(mine):

            for idx,val in enumerate(mine):
                counter[val]+=1
                if counter[val]<=2: index_sum[val]+=idx
        
        counter_and_index(list1)
        counter_and_index(list2)

        target = float('inf')
        key_sorted = sorted(index_sum.items(), key=lambda x:x[1])
        print(key_sorted)

        print(index_sum)
        ans = []
        for i,val in key_sorted:
            if counter[i]>=2 and index_sum[i]<=target:
                ans.append(i)
                target = index_sum[i]
        
        return ans

        


        
        