class Solution:
    def removeDuplicatesOne(self, nums) -> int:
        lastNum = None
        i = 0
        try:
            while True:
                num = nums[i]
                if lastNum == num:
                    nums.remove(num)
                else:
                    lastNum = num
                    i += 1
        except:
            pass
        return len(nums)
    def removeDuplicates(self, nums) -> int:
        length = len(nums)
        i = 0
        j = 1
        while j < length:
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
            j += 1
        return i + 1



li = [1,1,1,2,2,3,5,6,7,7,8]

print(Solution().removeDuplicates(li))