from collections import deque

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        que=deque()
        ans=[]

        for i in range (k):
            while (que and nums[que[-1]]<nums[i]):
                que.pop()
            que.append(i)

        ans.append(nums[que[0]])

        for i in range(k,len(nums)):
            while (que and nums[que[-1]]<nums[i]):
                que.pop()
            que.append(i)

            while que[0]<=i-k:
                que.popleft()

            ans.append(nums[que[0]])

        return ans