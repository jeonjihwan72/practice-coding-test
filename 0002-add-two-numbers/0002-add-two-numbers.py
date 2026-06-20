# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        # 시작을 도와줄 가짜(더미) 노드 생성
        dummy = ListNode(0)
        current = dummy
        
        carry = 0  # 올림수를 저장할 변수
        
        # l1이 남아있거나, l2가 남아있거나, 더해야 할 올림수(carry)가 남아있을 때까지 반복
        while l1 or l2 or carry:
            total = carry  # 이번 자릿수 합계에 이전 올림수를 먼저 더함
            
            # l1 노드가 존재하면 값을 더하고 다음 노드로 이동
            if l1:
                total += l1.val
                l1 = l1.next
                
            # l2 노드가 존재하면 값을 더하고 다음 노드로 이동
            if l2:
                total += l2.val
                l2 = l2.next
            
            # 새로운 올림수 계산
            carry = total // 10
            # 현재 노드에 저장할 일의 자리 값 계산
            val = total % 10
            
            # 결과 리스트에 새 노드 연결 후 포인터 이동
            current.next = ListNode(val)
            current = current.next
            
        # dummy는 0을 가리키고 있으므로, 진짜 결과는 dummy.next부터 시작됨
        return dummy.next