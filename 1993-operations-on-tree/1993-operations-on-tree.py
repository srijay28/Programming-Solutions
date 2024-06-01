class LockingTree:

    def __init__(self, parent: List[int]):
        self.root = TreeNode(0)
        self.root.parent = None
        self.d = {0:self.root}
        for i in range(1,len(parent)):
            node = TreeNode(i)
            self.d[i] = node
        for i,n in enumerate(parent):
            if i == 0:
                continue
            self.d[i].parent = self.d[n]


    def lock(self, num: int, user: int) -> bool:
        node = self.d[num]
        if node.isLocked:
            return False
        parent = node.parent
        while parent:
            parent.lockedDescendants.add(node)
            parent = parent.parent
        node.lockedBy = user
        node.isLocked = True
        return True

    def unlock(self, num: int, user: int) -> bool:
        node = self.d[num]
        if not node.isLocked or node.lockedBy != user:
            return False
        parent = node.parent
        while parent:
            parent.lockedDescendants.remove(node)
            parent = parent.parent

        node.lockedBy = -1
        node.isLocked = False
        return True

    def upgrade(self, num: int, user: int) -> bool:
        node = self.d[num]
        if node.isLocked or not node.lockedDescendants:
            return False
        parent = node.parent
        while parent:
            if parent.isLocked:
                return False
            parent = parent.parent
        descs = list(node.lockedDescendants)
        for desc in descs:
            self.unlock(desc.num,desc.lockedBy)
        self.lock(node.num,user)
        return True

class TreeNode:
    def __init__(self,num:int):
        self.num = num
        self.isLocked = False
        self.lockedBy = -1
        self.lockedDescendants = set()
        self.parent = None

    

    
# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)