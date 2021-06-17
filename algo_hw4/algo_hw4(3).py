class ListNode:
    def __init__(self, data:int):
        self.data = data
        self.next = None
    def __iter__(self):
        current = self
        while current is not None:
            yield current # suspend and output current ListNode object
            current = current.next

def init_list(seq:list)->ListNode:
    head = None
    for i in seq:
        if head is None:
            head = ListNode(i)
            tail = head
        elif type(i) is int and i < 0:
            for idx,n in enumerate(head): #idx is the index of the element and n is the element
                if idx == -1-i: #-1-i = -(i+1)
                    tail.next = n
                    break
        else:
            tail.next = ListNode(i)
            tail = tail.next
    return head

# has_cycle(init_list([1,2,3,4,5,6,7,8,-4])) -> 4
#       [1,2,3,4,5,6,7,8,-4] -> 1,2,3,4,5,6,7,8
# index: 0,1,2,3,4,5,6,7, 8           ^_______|

def search_rec(self,key):
    if self.data == key:
        return self
    elif self.next is None:
        return None
    else:
        return self.next.search_rec(key)

def has_cycle(head):
    ans_list = []
    for idx,ListNode in enumerate(head):
        if ListNode not in ans_list:
            ans_list.append(ListNode)
        else:
            return ListNode.data
    return None

print_list(init_list([1,2,3,4,5,6,7,8,-4]))