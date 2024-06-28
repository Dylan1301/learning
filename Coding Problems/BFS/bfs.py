from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def rightSideView(self, root):

    stack1, stack2 = deque(), deque()
    res = []
    stack1.append(root)

    while stack1:
        curr = stack1.popleft()
        print(curr)

        if curr and curr.left:
            stack2.append(curr.left)
        if curr and curr.right:
            stack2.append(curr.right)

        if not stack1:
            res.append(curr.val)
            stack1, stack2 = stack2, stack1
        
    return res


print(rightSideView("", TreeNode(1,TreeNode(2), None)))