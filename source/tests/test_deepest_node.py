import unittest
from deepest_node.binaryTree import binaryTree
from deepest_node import deepest_node_finder as finder

class DeepestNodeTests(unittest.TestCase):
    def test_deepestNode(self):
        expectedNodeData = "d"
        binaryTree = createBinaryTree()
        resultNode = finder.findDeepestNode(binaryTree)
        self.assertEqual(expectedNodeData, resultNode)
    

def createBinaryTree():
    tree = binaryTree("a")
    branchB = binaryTree("b")
    branchC = binaryTree("c")
    tree.left = branchB
    tree.right = branchC
    
    leafD = binaryTree("d")
    branchB.left = leafD
    return tree