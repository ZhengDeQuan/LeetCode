
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def addTwoNumbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """

    l3_head = ListNode(0)  # 弄一个无值的头
    l3 = ListNode(0)
    l3_head.next = l3

    while l1.next is not None and l2.next is not None:
        l3.val = l1.val + l2.val
        l3.next = ListNode(0)
        l3 = l3.next
        l2 = l2.next
        l1 = l1.next

    l3.val = l1.val + l2.val

    while l2.next is not None:
        l3.next = ListNode(l2.next.val)
        l3 = l3.next
        l2 = l2.next

    while l1.next is not None:
        l3.next = ListNode(l1.next.val)
        l3 = l3.next
        l1 = l1.next

    # 清前导0
    # while l3_head.val == 0:
    #     l3_head = l3_head.next
    #     if l3_head is None:
    #         break
    # if l3_head is None:
    #     return ListNode(0)

    temp = l3_head
    carry = 0  # 低位的进位
    while l3_head.next is not None:
        temp_val = l3_head.val + carry
        l3_head.val = temp_val % 10
        carry = int(temp_val / 10)
        l3_head = l3_head.next
    temp_val = l3_head.val + carry
    l3_head.val = temp_val % 10
    carry = int(temp_val / 10)
    if carry > 0:
        l3_head.next = ListNode(carry)

    return temp.next


def makeListNode(temp: list):
    if temp == [] :return None
    head = ListNode(0)
    cur = head
    for ele in temp:
        tempNode = ListNode(ele)
        cur.next = tempNode
        cur = cur.next
    return head.next
def Write(C):
    while C:
        print(C.val)
        C = C.next

if __name__ == "__main__":
    A = makeListNode([9,8])
    Write(A)
    B = makeListNode([1])
    Write(B)
    C = addTwoNumbers(A,B)
    Write(C)






