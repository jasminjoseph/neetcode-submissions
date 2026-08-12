# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True

        pque = deque()
        pque.append(p)

        qque = deque()
        qque.append(q)

        while pque and qque:
            for i in range(len(pque)):
                pnode = pque.popleft()
                qnode = qque.popleft()

                if pnode is None and qnode is None:
                    continue
                if pnode is None or qnode is None or pnode.val != qnode.val:
                    return False
                
                pque.append(pnode.left)
                pque.append(pnode.right)
                qque.append(qnode.left)
                qque.append(qnode.right)

        return True

    

        