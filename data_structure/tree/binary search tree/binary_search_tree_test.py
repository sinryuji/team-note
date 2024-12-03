from binary_search_tree import BinarySearchTree

array = [40, 4, 34, 45, 14, 55, 48, 13, 15, 49, 47]

bst = BinarySearchTree()
for x in array:
    bst.insert(x)

# Find
print(bst.find(15))  # True
print(bst.find(17))  # False
