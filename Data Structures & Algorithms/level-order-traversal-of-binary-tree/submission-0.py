# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        retList = []

        que = deque()
        que.append(root)

        while que:
            ret = []
            for i in range(len(que)):
                node = que.popleft()
                ret.append(node.val)

                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)

            retList.append(ret)  
        return retList