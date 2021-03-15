class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        minlen = 0
        start = 0
        end = 0
        sum = 0

        while end < len(nums):
            sum += nums[end]
            while start <= end and sum >= target :
                if minlen == 0:
                    minlen = end - start + 1
                else:
                    minlen = min(minlen, end - start + 1)
                sum -= nums[start]
                start += 1
            end += 1

        return minlen

if __name__ == '__main__':
    print Solution.minSubArrayLen(Solution(), 7, [2,3,1,2,4,3])