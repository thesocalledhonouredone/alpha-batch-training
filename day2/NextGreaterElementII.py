class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        st = list()
        n = len(nums)

        res = [-1] * n
        
        for i in range(2*n-1, -1, -1):
            while len(st) != 0 and nums[i%n] >= nums[st[-1]]:
                st.pop()
            if len(st) != 0:
                res[i%n] = nums[st[-1]]
            st.append(i%n)

        return res

        