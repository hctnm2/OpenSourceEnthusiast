#brute - not efficient
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        largest = []
        
        if len(nums) == 1:
            return nums[0]
        else:
            for i in range(len(nums)):
                temp = 0
                largest.append(nums[i])
                for j in range(i+1, len(nums)):
                    if j == i+1:
                        temp = temp + nums[i] + nums[j]
                        largest.append(temp)
                    else:
                        temp = temp + nums[j]
                        largest.append(temp)
                maxEle = max(largest)
                largest.clear()
                largest.append(maxEle)

            return max(largest)

# Optimized to O(n)

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        curSum = 0
        
        for n in nums:
            if curSum < 0:
                curSum = 0
            curSum += n
            maxSum = max(maxSum, curSum)
        return maxSum
            