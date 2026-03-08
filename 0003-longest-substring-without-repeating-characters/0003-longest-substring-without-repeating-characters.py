class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}  # 字典记录：{字符: 该字符最后出现的下标}
        left = 0  # 左指针初始化
        max_len = 0  # 结果记录
        
        for right, char in enumerate(s):  # enumerate 同时拿到下标和字符，非常 Pythonic
            if char in char_map:  # 发现当前字符之前出现过
                # 核心逻辑：左指针直接跳到【重复位置+1】和【当前left】的较大值
                # 为什么要取 max？防止 left 往回跳（后面踩坑会讲）
                left = max(left, char_map[char] + 1)
            
            char_map[char] = right  # 更新或插入当前字符的最新位置
            max_len = max(max_len, right - left + 1)  # 计算当前窗口长度
            
        return max_len  # 搞定，收工