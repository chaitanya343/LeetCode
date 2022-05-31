class TreeNode():
    def __init__(self, s, e):
        self.s = s
        self.e = e
        self.left = None
        self.right = None
        
    def insert(self, node):
        if node.s >= self.e:
            
        if node.e <= self.s:
            # Left side
            if self.left is not None:
                return self.left.insert(node)
            else:
                self.left = node
                return True
        return False

class MyCalendar:
    def __init__(self):
        self.root = None
        self.store = {}

    def book(self, start, end):
        # Brute force - O(N^2)
        for bookedStart, bookedEnd in self.store.items():
            if bookedStart<end and start<bookedEnd:
                # print(bookedStart, "<", end, start, "<", bookedEnd)
                return False
        self.store[start] = end
        return True

    def book_bst(self, start, end):
        # Optimized with a BST
        if self.root is not None:
            return self.root.insert(TreeNode(start, end))
        else:
            self.root = TreeNode(start, end)
            return True


obj = MyCalendar()
# print(obj.book(10, 20))
# print(obj.book(20, 25))
# print(obj.book(30, 35))

# print(obj.book(15, 25))
# print(obj.book(25, 32))

print(obj.book_bst(10, 20))
print(obj.book_bst(20, 25))
print(obj.book_bst(30, 35))

print(obj.book_bst(15, 25))
print(obj.book_bst(25, 32))
