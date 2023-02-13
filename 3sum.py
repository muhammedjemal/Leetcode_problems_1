class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums = sorted(nums)
        
        for idx, val in enumerate(nums[:-2]):
            if val>0:
                break
            if val == nums[idx -1] and idx>0:
                continue
            left_point = idx+1
            right_point = len(nums)-1
            
            while left_point<right_point:
                three_sum = nums[left_point]+nums[right_point]+val
                if three_sum == 0:
                    output.append([nums[left_point], nums[right_point], val])
                if three_sum > 0:
                    right_point -=1
                else:
                    left_point +=1
                    while nums[left_point] == nums[left_point-1] and left_point<right_point:
                        left_point +=1
        return output  
 
     
