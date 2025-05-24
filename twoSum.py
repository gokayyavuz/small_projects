class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        SumList = []
        for i in range(len(nums)):
            tmp_x = nums[i]
            tmp_target = target - tmp_x
            for j in range(len(nums)):
                if i != j and tmp_target - nums[j] == 0:
                    SumList.append(i)
                    SumList.append(j)
                    return SumList
