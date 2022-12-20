ops = 0 # operation counter

# Definition for singly-linked list.
class ListNode:
    # 3 per call
    def __init__(self, x): 
        self.val = x
        self.next = None



class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        global ops
        x1 = 0
        x2 = 0
        count = 0

        ops += 3 # assignments

        while l1!=None and l2!=None:
            ops += 3 # comparison + and + comparison = 3
            x1 += l1.val * 10**count 
            ops += 4 # += , * , ** = 4
            x2 += l2.val * 10**count
            ops += 4 # += , * , ** = 4
            l1 = l1.next 
            ops += 1 # assignment = 1
            l2 = l2.next 
            ops += 1 # assignment = 1
            count += 1 
            ops += 2 # assignment , + = 2
        print(f"loop one finished at ops: {ops}")
        flg = False
        ops += 1
        while l1!=None: 
            ops += 1 # comparison = 1
            flg = True
            x1 += l1.val * 10**count
            ops += 4 # assignment , + , * , ** + 4
            l1 = l1.next
            ops += 1 # assignment = 1
            count += 1
            ops += 2 # assignment , +  = 2

        if flg:
            print("Flag one activated")
            ops -= 1

        print(f"loop two finished at ops: {ops}")
        flg = False
        ops += 1
        while l2!=None:
            ops += 1 # comparison = 1
            flg = True
            x2 += l2.val * 10**count 
            ops += 4 # assignment , + , * , ** = 4
            l2 = l2.next 
            ops += 1 # assignment = 1
            count += 1
            ops += 2 # assignment, + = 2

        if flg:
            print("Flag two activated")
            ops -= 1

        print(f"loop three finished at ops: {ops}")
        ans = x1 + x2
        ops += 2 # assignment, + = 2
        head = ListNode(ans % 10)
        ops += 5 # assignment + mod + function call + 2 for constructor = 5
        ans //= 10 
        ops += 2 # assignment , + = 2
        n1 = head
        ops += 1 # assignment = 1

        while ans:
            ops += 1 # comparison ans != 0 , = 1
            n1.next = ListNode(ans % 10)
            ops += 5  # assignment + mod + function call + 2 for constructor = 5
            ans //= 10 
            ops += 2 # assignment , + = 2
            n1 = n1.next
            ops += 1 # assignment = 1
        ops += 1
        print(f"loop four finished at ops: {ops}")
        return head

sol = Solution()
l1 = ListNode(1)

l2 = ListNode(9)
l2.next = ListNode(9)
res = sol.addTwoNumbers(l1, l2)
while res:
    print(res.val)
    res = res.next
print(f"ops: {ops}")
