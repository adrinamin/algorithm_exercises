import sys
from deepest_node.binaryTree import binaryTree


def __creatBinaryTreeFrom(treeConnections: list):
    tree = binaryTree(treeConnections[0])
    branchB = binaryTree(treeConnections[1])
    branchC = binaryTree(treeConnections[2])
    tree.left = branchB
    tree.right = branchC
    leafD = binaryTree(treeConnections[3])
    branchB.left = leafD
    
    return tree


def find(tree: binaryTree, level, maxLevel, res):
    """finds the maxLevel of the depest node inside a binary tree

    Args:
        tree (binaryTree): The binary tree which is searched
        level (int): The levels seen so far
        maxLevel (list): the maximum level of the tree
        res (list): value of the deepest node so far
    """
    if tree != None:
        level += 1
        find(tree.left, level, maxLevel, res)
        
        if level > maxLevel[0]:
            res[0] = tree.nodeData
            maxLevel[0] = level
        
        find(tree.right, level, maxLevel, res)
  

def findDeepestNode(tree: binaryTree):
    # Initialze result and max level
    res = [-1]
    maxLevel = [-1]
 
    # Updates value "res" and "maxLevel"
    # Note that res and maxLen are passed
    # by reference.
    find(tree, 0, maxLevel, res)
    return res[0]
    

def main(treestring: str):
    """Creates a binary tree from a sting with branch and leaf values
    The string should have the following form:
    e.g: a,b,c,d
    The above code gives the following tree:
                    a
                   / \
                  b   c
                 /
                d
    
    The comma between the connections is mandatory! The first element is considerered to be the root.
    
    Args:
        treestring (str): The string with the branch and leaf connections
    """
    treeConnections = treestring.split(",")
    tree = __creatBinaryTreeFrom(treeConnections)
    findDeepestNode(tree)

if __name__ == '__main__':
    main(sys.argv[1])