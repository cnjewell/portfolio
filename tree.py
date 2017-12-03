# tree data type pattern
# heaps
# tree transversal

# value, left right


# TODO: TreeNode class
# TODO: Class methods: render, insert, has_value, remove
# TODO: Invert Binary tree, render inversion, save directional switch for subsequent insertions


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def get_list(self):
        """ Returns list of tree values """
        return_left = []
        return_right = []

        if self.left is not None:
            return_left = self.left.get_list()

        if self.right is not None:
            return_right = self.right.get_list()

        return return_left + [self.val] + return_right

    def insert(self, val):
        """ Insert val in root """ 
        if val == self.val:
            return None

        elif val > self.val:
            if self.right is not None:
                self.right.insert(val)
            else:
                self.right = TreeNode(val)

        elif val < self.val:
            if self.left is not None:
                self.left.insert(val)
            else:
                self.left = TreeNode(val)

    def has_value(self, val):
        """ Returns True if val in is tree """

        if self.val == val:
            return True

        elif self.left == None and self.right == None:
            return False

        else:
            if self.left is not None:
                return self.left.has_value(val)
            
            if self.right is not None:
                return self.right.has_value(val)
            


# def has_value(root, val):
#     """ Returns True if val in is tree """
    
#     if root.val == val:
#         return True

#     elif root.left == None and root.right == None:
#         return False

#     else:
#         if root.left  is not None:
#             return has_value(root.left,  val)

#         if root.right is not None:
#             return has_value(root.right, val)
    

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

        if not has_value(root, val):
            return None
    
        if root.val == val:
            return None
        

def main():

    root = TreeNode(5)
    print(root.val)

    root.left = TreeNode(3)
    root.right = TreeNode(7)

    print(root.get_list())

    root.insert(9)
    print(root.get_list())
    root.insert(1)
    print(root.get_list())
    root.insert(6)
    print(root.get_list())
    root.insert(8)
    print(root.get_list())
    root.insert(2)
    print(root.get_list())
    root.insert(4)
    print(root.get_list())
    root.insert(5)
    print(root.get_list())

    print()
    print(root.has_value(5))
    print(root.has_value(2))
    print(root.has_value(10))

    tree2 = TreeNode(3)
    print(tree2.has_value(5))

    print()

    print(root.get_list())

if __name__ == "__main__":
    main()