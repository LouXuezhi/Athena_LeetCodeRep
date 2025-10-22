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
            if len(que)==0:
                que.append(nums[i])
            else:
                if nums[i]<=que[-1]:
                    if len(que)<k:
                        que.append(nums[i])
                    else:
                        que.clear()
                        que.append(nums[i])
                if nums[i]>que[-1] and nums[i]<que[0]:
                    while (nums[i]>que[-1]):
                        que.pop()
                    que.append(nums[i]) 
                if nums[i]>=que[0]:
                    que.clear()
                    que.append(nums[i])
                   
        ans.append(que[0])
        for i in range (len(nums)-k):
            p=k+i
            if len(que)>=k:
                que.popleft()
            if len(que)==0:
                que.append(nums[p])
            else:
                if nums[p]<=que[-1]:
                    que.append(nums[p])
                if nums[p]>que[-1] and nums[p]<que[0]:
                    while (nums[p]>que[-1]):
                        que.pop()
                    que.append(nums[p])
                if nums[p]>=que[0]:
                    que.clear()
                    que.append(nums[p])

            ans.append(que[0])

        return ans


        
# 不能完成 原因是在使用值做队列的时候其实放弃了index信息
# 下次注意要用 Index 做队列


