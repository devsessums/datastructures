import sys

class BNode():
    def __init__(self, root=None, left=None, right=None, val=0.0):
        try:
            self.root = root
            self.left = left
            self.right = right
            self.val = val
        except Exception as e:
            print(e)

    @property
    def root(self):
        return _root

    @root.setter
    def root(self, root):
        if (type(root) == type(BNode) or type(root) == type(None)):
            self._root = root
        else:
            raise TypeError("Root Node was type {}. Expected {}.".format(type(root), 'BNode'))

    @property
    def left(self):
        return _left

    @left.setter
    def left(self, left):
        if (type(left) == type(BNode) or type(left) == type(None)):
            self._left = left
        else:
            raise TypeError("Left Node was type {}. Expected {}.".format(type(left), 'BNode'))

    @property
    def right(self):
        return _right

    @right.setter
    def right(self, right):
        if (type(right) == type(BNode) or type(right) == type(None)):
            self._right = right
        else:
            raise TypeError("Right Node was type {}. Expected {}.".format(type(right), 'BNode'))

    @property
    def val(self):
        return _val

    @val.setter
    def val(self, val):
        if (type(val) != float):
            raise TypeError("Got {}. Expected {}.".format(type(val), 'float'))
        self._val = val

    def __str__(self):
        print("here")
        try:
            str = "{}".format(self._val)
            return str
        except Exception as e:
            print(e)

class PNode():
    def __init__(self, nodes=[], val=None):
        try:
            self.nodes = nodes
            self.val = val
            self.size = len(nodes)
        except Exception as e:
            print(e)

    def __str__(self):
        try:
            str = "{}".format(self._val)
            return str
        except Exception as e:
            print(e)

# i for imaginary as way of saying this is a complex BNode
# iBNode extends BNode to have more generic property:value information
class iBNode(BNode):
    def __init__(self, root=None, left=None, right=None, val=0.0, **propList):
        super().__init__(root=root, left=left, right=right, val=val)
        self.prop_list = propList

    @property
    def prop_list(self):
        print("sending prop_list")
        return _prop_list

    @prop_list.setter
    def prop_list(self, propList):
        if (type(propList) != dict):
            raise TypeError("Got {}. Expected {}.".format(type(propList), 'dict'))
        # Expect supplied functions for computing the value of a node to be valid
        self._prop_list = propList



if __name__ == '__main__':
    print(sys.argv)
#i = iBNode(cpu=2, jobs=10, est_time_per_job=600)
