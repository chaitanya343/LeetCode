# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


def getIntersectionNode_withSet(headA, headB):
    # Store 1 list in a Set and Seach each of the other in the set
    setA = set()
    while headA != None:
        setA.add(headA)
        headA = headA.next
    
    while headB != None:
        if headB in setA:
            return headB
        headB = headB.next
    
    return None

def getIntersectionNode(headA, headB):
    # Get the difference in length, bring the longer one equal to the shorter one, now check each simultaneously
    lenA = 0
    lenB = 0
    
    pa = headA
    pb = headB
    while pa!=None:
        lenA+=1
        pa = pa.next
    while pb!=None:
        lenB+=1
        pb = pb.next
        
    if lenA > lenB:
        jump = lenA-lenB
        for _ in range(jump):
            headA = headA.next
    else:
        jump = lenB-lenA
        print(jump)
        for _ in range(jump):
            headB = headB.next
    
    while headA!=None or headB!=None:
        if headA == headB:
            return headA
        headA = headA.next
        headB = headB.next
    
    return None