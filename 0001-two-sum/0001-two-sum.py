class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # 创建一个字典，用来存放：数字 -> 它的下标
        # 底层逻辑：这就像工厂里的扫码枪，扫一下零件（数字），立马就能查到它在哪个架子上（下标）
        hashmap = {}
        
        for i, num in enumerate(nums):
            # 计算我们需要寻找的那个“另一半”
            complement = target - num
            
            # 如果“另一半”已经在字典里了，直接收工！
            if complement in hashmap:
                return [hashmap[complement], i]
            
            # 如果不在，就把当前的数字和下标存进去
            hashmap[num] = i