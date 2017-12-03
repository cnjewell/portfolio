# tree data type pattern
# heaps
# tree transversal

# value, left right

# TODO: TreeNode class
# TODO: Class methods: render, insert, has_value, remove
# TODO: Invert Binary tree, render inversion, save directional switch for subsequent insertions

class TreeNode:
    def __init__(self, val, parent=None):
        self.val = val
        self.parent = parent
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
                self.right = TreeNode(val, self)

        elif val < self.val:
            if self.left is not None:
                self.left.insert(val)
            else:
                self.left = TreeNode(val, self)

    def has_value(self, val):
        """ Returns True if val in is tree, False if not """

        if self.val == val:
            return True

        elif self.left == None and self.right == None:
            return False

        else:
            if self.left is not None:
                return self.left.has_value(val)
            
            if self.right is not None:
                return self.right.has_value(val)


    def lowest_value(self):
        """Returns child node with lowest value. Returns self if there are no children"""

        if self.left == None:
            return self.val
        else:
            return self.left.lowest_value()


    def remove(self, val, parent=None):
        """ Remove val from TreeNode root. Returns None if val is not in tree or if root is val and is the only node. """
        
        # target found
        if self.val == val:
            
            # if target is has no parent and has no children
            if self.left == None and self.right == None and parent == None:
                return None

            # Target has no children, simply set link to parent with None
            elif self.left == None and self.right == None:
                if parent.left == self:
                    parent.left = None
                else:
                    parent.right = None

            # Target has one child
            # Replace target's parent's reference with only child
            elif self.left == None or self.right == None:
                if parent == None:
                    self.val = self.right.lowest_value()
                    self.right.remove(self.val, self)
                else:
                    if parent.left == self:
                        if self.left != None:
                            parent.left = self.left
                        else:
                            parent.left = self.right
                    else:
                        if self.left != None:
                            parent.right = self.left
                        else:
                            parent.right = self.right

            # Target has two children
            # Find lowest_child() of right-hand branch
            # The move min value to target val and None the lowest child
            else: 
                self.val = self.right.lowest_value()
                self.right.remove(self.val, self)

        # can I keep searching?
        elif self.left == None and self.right == None:
            return None
        
        # keep searching for target
        else:
            if self.left is not None:
                self.left.remove(val, self)
            if self.right is not None:
                self.right.remove(val, self)



    def __str__(self):
        return "{TreeNode: val=" + str(self.val) + "}"
        

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

    print(root.lowest_value())

    root.remove(1)
    print(root.get_list())
    root.remove(1)
    print(root.get_list())
    root.remove(2)
    print(root.get_list())
    root.remove(3)
    print(root.get_list())
    root.remove(4)
    print(root.get_list())
    root.remove(5)
    print(root.get_list())




    print()

    print(root.get_list())

if __name__ == "__main__":
    main()