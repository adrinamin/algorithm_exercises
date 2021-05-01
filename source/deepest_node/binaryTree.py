class binaryTree:
    def __init__(self, nodeData, left=None, right=None):
        self.nodeData = nodeData
        self.left = left
        self.right = right
        self.visited = False
        
    
    def __str__(self):
        return str(self.nodeData)