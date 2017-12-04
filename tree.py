# tree data type pattern
# heaps
# tree transversal

# value, left right

# TODO: TreeNode class
# TODO: Class methods: render
# TODO: Invert Binary tree, render inversion, save directional switch for subsequent insertions

class Tree:
    def __init__(self):
        self.root = None

    def get_list(self):
        if self.root == None:
            return None
        else:
            return self.root.get_list()

    def insert(self, val):
        if self.root == None:
            self.root = TreeNode(val)
        else:
            self.root.insert(val)

    def has_value(self, val):
        if self.root == None:
            return None
        else:
            return self.root.has_value(val)

    def lowest_value(self):
        if self.root == None:
            return None
        else:
            return self.root.lowest_value()

    def remove(self, val):
        if self.root == None:
            return None
        elif val == self.root.val:
            dummy_root = TreeNode(0)
            dummy_root.right = self.root
            dummy_root.remove(val)
            self.root = dummy_root.right
        else:
            return self.root.remove(val)

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

        return_list = return_left + [self.val] + return_right
        if return_list == [None]:
            return None
        else:
            return return_list

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
        """ 
        Remove val from binary search tree.
        Returns None if val is not in tree. 
        If val is the only node....
        """
        
        # target found
        if self.val == val:
            
            # if target has no parent and has no children
            if self.left == None and self.right == None and parent == None:
                self.val = None
                return None

            # Target has no children, simply set link to parent with None
            elif self.left == None and self.right == None:
                if parent.left == self:
                    parent.left = None
                else:
                    parent.right = None

            # Target has one child
            # Replace target's parent's reference with only child, if there is a parent
            elif self.left == None or self.right == None:
                # if parent == None: 
                #     if self.left != None:
                #         self.val = self.left.val
                #         self.left.remove(self.val, self)
                #     elif self.right != None:
                #         self.val = self.right.val
                #         self.right.remove(self.val, self)

                # else:
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
            # Find lowest_value of right-hand branch
            # The move min value to target val and None the lowest child
            else: 
                self.val = self.right.lowest_value()
                self.right.remove(self.val, self)


        # can I keep searching?
        elif self.left == None and self.right == None:
            return None
        
        # keep searching for target
        else:
            if val < self.val:
                if self.left is not None:
                    self.left.remove(val, self)

            elif val > self.val:
                if self.right is not None:
                    self.right.remove(val, self)
            else:
                return None


    def __str__(self):
        return "{TreeNode: val=" + str(self.val) + "}"
        

def main():

    root = Tree()
    
    root.insert(3)
    root.insert(7)
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
    
    print()
    
    print(root.lowest_value())
    
    print()
    
    root.remove(5)
    print(root.get_list())
    root.remove(3)
    print(root.get_list())
    root.remove(7)
    print(root.get_list())
    root.remove(4)
    print(root.get_list())
    root.remove(9)
    print(root.get_list())
    root.remove(2)
    print(root.get_list())
    root.remove(1)
    print(root.get_list())
    root.remove(7)
    print(root.get_list())
    root.remove(8)
    print(root.get_list())

    print()

    print(root.get_list())

if __name__ == "__main__":
    main()