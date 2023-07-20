def name():
    return "Tree sort"


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def insert(self, val):
        if self.val:
            if val < self.val:
                if self.left is None:
                    self.left = Node(val)
                else:
                    self.left.insert(val)
            elif val > self.val:
                if self.right is None:
                    self.right = Node(val)
                else:
                    self.right.insert(val)
        else:
            self.val = val


def inorder(root, res):
    if root:
        inorder(root.left, res)
        res.append(root.val)
        inorder(root.right, res)


def sort(arr):
    if len(arr) == 0:
        return arr
    root = Node(arr[0])
    for i in range(1, len(arr)):
        root.insert(arr[i])
    res = []
    inorder(root, res)
    return res