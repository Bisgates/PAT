
class TreeNode:
	def __init__(self,x):
		self.val = x
		self.left = None
		self.right = None

post_lis = []

class Tree:
	def postOrder(self,root):
		if(root):
			self.postOrder(root.left)
			self.postOrder(root.right)
			post_lis.append(root.val)

	def build(self,preOrder,inOrder):
		if(preOrder):
			k = inOrder.index(preOrder.pop(0))
			root = TreeNode(inOrder[k])
			root.left = self.build(preOrder,inOrder[:k])
			root.right = self.build(preOrder,inOrder[k+1:])
		return root

pre=[1,2,3,4,5,6]
ino=[3,2,4,1,6,5]

root = Tree().build(pre,ino)
# print(Tree().postOrder(root))
