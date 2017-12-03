# tree data type pattern
# heaps
# tree transversal

# value, left right


# TODO: TreeNode class
# TODO: Class methods: list_all, render, insert, contains, remove
# TODO: Invert Binary tree, render inversion, save directional switch for subsequent insertions


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def get_list(root):
    """ Returns list of tree values """
    
    if root.left is not None:
        left = get_list(root.left)
    else:
        left = []

    if root.right is not None:
        right = get_list(root.right)
    else:
        right = []

    return left + [root.val] + right


def insert(root, val):
    """ Insert val in root """ 
    
    if val > root.val:
        if root.right is not None:
            insert(root.right, val)
        else:
            root.right = TreeNode(val)
    
    elif val < root.val:
        if root.left is not None:
            insert(root.left, val)
        else:
            root.left = TreeNode(val)
    
    elif val == root.val:
        return None


def tree_search(root, val):
    """ Returns True if val in is tree """
    
    if root.val == val:
        return True

    elif root.left == None and root.right == None:
        return False

    else:
        if root.left  is not None:
            return tree_search(root.left,  val)

        if root.right is not None:
            return tree_search(root.right, val)
    

def remove(root, val):
    """ Remove val from TreeNode root. Return None if val is not in tree. """
    # first, is val even in this tree? If not, return None

    # find the TreeNode in this tree that has the cargo 'val'
    # once you find that TreeNode, 
        # Set the upstream node's left/right to None
        # Take the clipped TreeNode and for each connected node, insert their cargoes into root
            # Do not include the clipped TreeNode's cargo in that run of insertions

    # base case(s)
        # Only 1 TreeNode equal to the value, return error?
            # no last_tree
        # Only 2 last_tree, this_tree

    # Solution outline
    # When removing a node, 
        # find the lowest child of the target node
        # replace the removed node with the lowest child
    
    first_pass = False
    if first_pass:

        if not tree_search(root, val):
            return None
    
        if root.val == val:
            return None
        

def main():

    root = TreeNode(5)
    print(root.val)

    root.left = TreeNode(3)
    root.right = TreeNode(7)

    print(get_list(root))

    insert(root, 9)
    print(get_list(root))
    insert(root, 1)
    print(get_list(root))
    insert(root, 6)
    print(get_list(root))
    insert(root, 8)
    print(get_list(root))
    insert(root, 2)
    print(get_list(root))
    insert(root, 4)
    print(get_list(root))

    print()
    print(tree_search(root, 5))
    print(tree_search(root, 2))
    print(tree_search(root, 10))

    tree2 = TreeNode(3)
    print(tree_search(tree2, 5))

    print()

    print(get_list(root))

if __name__ == "__main__":
    main()