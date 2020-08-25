# print values of a tree in an in-order fashion


# binary tree class
class Node:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

# using recursion
def in_order(node):
	if node is None:
		return
	
	in_order(node.left)
	print(node.val)
	in_order(node.right)

# usign interaction
def in_order_iteractive(node):
	stack = []
	while (stack or node is not None):
		if node is not None:
			stack.append(node)
			node = node.left
		else:
			node = stack.pop()
			print(node.val)
			node = node.right

# instance of the binary tree
root = Node(12)
root.left = Node(6)
root.right = Node(4)


in_order(root)
in_order_iteractive(root)


# time O(n) - n is the number of nodes of the tree
# space O(h) - h is the height of the tree
# worst case scenario - unbalanced tree, the height of the tree is n => O(n)