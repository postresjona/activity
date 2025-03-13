class TreeNode: 
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

#In-Order Traversal
def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.value, end = " ")
        inorder_traversal(root.right)

#Pre-0rder Traversal
def preorder_traversal(root):
    if root: 
        print(root.value, end = " ")
        preorder_traversal(root.left)
        preorder_traversal(root.right)

#Post Order Traversal
def postorder_traversal(root):
    if root:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.value, end = " ")

#Swap Inorder
def swap_inorder_traversal(root):
    if root: 
        swap_inorder_traversal(root.right)
        print(root.value, end = " ")
        swap_inorder_traversal(root.left)

#Swap Pre-Order
def swap_preorder_traversal(root):
    if root:
        print(root.value, end = " ")
        swap_preorder_traversal(root.right)
        swap_preorder_traversal(root.left)

#Swap Post Order
def swap_postorder_traversal(root):
    if root: 
        swap_postorder_traversal(root.right)
        swap_postorder_traversal(root.left)
        print(root.value, end = " ")

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

print("In-order traversal")
inorder_traversal(root)
print("\nPre-order Traversal")
preorder_traversal(root)
print("\nPost Order Trversal")
postorder_traversal(root)
print(" ")
print("\nAfter Swapping")
print("\nInorder Traversal")
swap_inorder_traversal(root)
print("\nPre-order Traversal")
swap_preorder_traversal(root)
print("\nPost Order Traversal")
swap_postorder_traversal(root)