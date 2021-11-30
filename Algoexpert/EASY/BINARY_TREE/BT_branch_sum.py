#             1
#            /   \
#           2     3
#        /    \   / \
#       4      5  6  7
#      / \     /
#     8   9   10
# sample output  [15, 16, 18, 10, 11]

# Recursively traverse the binary tree in depth first search like fashion
# and pass a running sum of the values of every previously visited node to each node that you are traversing

#O(n) time | O(n) space where n is the no.of nodes in the binary tree.

class BranchSum:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def branchSums(root):
    sums = []
    print("I am Branch Sums")
    calculateBranchSums(root, 0, sums)
    return sums

def calculateBranchSums(node, runningSum, sums ):
    print("I am branch sum helper")
    if node is None:
        return

    newRunningSum = runningSum + node.value
    print(node.value, newRunningSum, sums)
    if node.left is None and node.right is None:
        sums.append(newRunningSum)
        return
    print("Node.left")
    calculateBranchSums(node.left, newRunningSum, sums)
    print("Node.right")
    calculateBranchSums(node.right, newRunningSum, sums)


root = BranchSum(1)
root.left = BranchSum(2)
root.left.left = BranchSum(4)
root.left.right = BranchSum(5)
root.left.right.left = BranchSum(10)
root.left.left.left = BranchSum(8)
root.left.left.right = BranchSum(9)
root.right = BranchSum(3)
root.right.left = BranchSum(6)
root.right.right = BranchSum(7)
print(branchSums(root))





