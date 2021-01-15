# created by KUMAR SHANU

# 4. Score of Parentheses
# https://leetcode.com/problems/score-of-parentheses/


class TreeNode():
    def __init__(self, data=None):
        self.data = data
        self.parent = None
        self.children = []

    def addChild(self, child):
        self.children.append(child)

    def setParent(self, parent):
        self.parent = parent

    def getParent(self):
        return self.parent

    def getScore(self):
        if self.children == []:
            return 1
        res = 0
        for current in self.children:
            res += current.getScore()
        if self.parent == None:
            return res
        else:
            return 2 * res


class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        root = self.createTree(S)
        return root.getScore()

    def createTree(self, s):
        current = TreeNode()
        root = current
        for l in s:
            if l == '(':
                child = TreeNode()
                child.setParent(current)
                current.addChild(child)
                current = child
            else:
                current = current.getParent()

        return root
