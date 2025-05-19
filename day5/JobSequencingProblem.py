class Solution:
    def jobSequencing(self, deadline, profit):
        # code here
        
        deadline = [val for _, val in sorted(zip(profit, deadline))]
        deadline = deadline[::-1]
        profit.sort(reverse=True)

        slot = [0] * (max(deadline)+1)
        
        # print(profit, deadline, slot)

        for ind, ele in enumerate(profit):
            temp = deadline[ind]
            while temp >= 1:
                if slot[temp] == 0:
                    slot[temp] = ele
                    break
                temp -= 1

        profitSum = sum(slot)
        count = 0
        for i in slot:
            if i != 0:
                count += 1
        
        return [count, profitSum]


obj = Solution()

deadline = [2, 1, 2, 1, 1]
profit = [100, 19, 27, 25, 15]

print(obj.jobSequencing(deadline, profit))