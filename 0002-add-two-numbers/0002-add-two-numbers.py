class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        curr = dummy = ListNode(0) # 同时初始化木桩和工人
        carry = 0
        
        while l1 or l2 or carry:
            # 直接把值加到 carry 上
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            
            # divmod 同时算出 (商, 余数)，即 (新进位, 车厢数值)
            carry, val = divmod(carry, 10)
            
            curr.next = ListNode(val) # 挂新车
            curr = curr.next           # 挪位置
            
        return dummy.next