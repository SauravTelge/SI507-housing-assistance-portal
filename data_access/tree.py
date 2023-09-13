import json
import pickle
from extra_files.save_file import readWriteFile


class bstNode:
    """
    Binary Search Tree Node that defines basic operations for BST.

    Attributes
    ----------
    val : Any
        The value of the node.
    key : Any
        The key of the node.
    left : BSTNode
        Pointer to the left child.
    right : BSTNode
        Pointer to the right child.
    """

    def __init__(self, val=None, key=None):
        """
        Initialize a new BST node.

        Parameters
        ----------
        val : Any, optional
            The value of the node.
        key : Any, optional
            The key of the node.
        """
        self.left = None
        self.right = None
        self.val = val
        self.key = key

    def insert(self, val, key):
        """
        Insert a value with its corresponding key into the BST.

        Parameters
        ----------
        val : Any
            The value to be inserted.
        key : Any
            The key corresponding to the value.
        """
        if not self.val:
            self.val = val
            self.key = key
            return

        if self.key == key:
            return

        if key < self.key:
            if self.left:
                self.left.insert(val, key)
                return
            self.left = bstNode(val, key)
            return

        if self.right:
            self.right.insert(val, key)
            return
        self.right = bstNode(val, key)

    def delete(self, val, key):
        """
        Delete a node with a given value and key from the BST.

        Parameters
        ----------
        val : Any
            The value to be deleted.
        key : Any
            The key corresponding to the value.

        Returns
        -------
        BSTNode
            The root of the modified BST.
        """
        if self == None:
            return self
        if val < self.val:
            if self.left:
                self.left = self.left.delete(val, key)
            return self
        if val > self.val:
            if self.right:
                self.right = self.right.delete(val, key)
            return self
        if self.right == None:
            return self.left
        if self.left == None:
            return self.right
        min_larger_node = self.right
        while min_larger_node.left:
            min_larger_node = min_larger_node.left
        self.val = min_larger_node.val
        self.right = self.right.delete(min_larger_node.val, min_larger_node.key)
        return self

    def exists(self, key):
        """
        Check if a node with a given key exists in the BST.

        Parameters
        ----------
        key : Any
            The key to be checked.

        Returns
        -------
        Any
            The value associated with the key if it exists. False otherwise.
        """
        print("key", key)
        print("stored key", self.key)
        if key == self.key:
            return self.val

        if key < self.key:
            if self.left == None:
                return False
            return self.left.exists(key)

        if self.right == None:
            return False
        return self.right.exists(key)

    def get_min(self):
        """
        Return the minimum value node in the BST.

        Returns
        -------
        Any
            Minimum value present in the BST.
        """
        current = self
        while current.left is not None:
            current = current.left
        return current.val

    def get_max(self):
        """
        Return the maximum value node in the BST.

        Returns
        -------
        Any
            Maximum value present in the BST.
        """
        current = self
        while current.right is not None:
            current = current.right
        return current.val

    def preorder(self, vals):
        """
        Pre-order traversal of the BST.

        Parameters
        ----------
        vals : list
            A list to store values during traversal.

        Returns
        -------
        list
            List of values in pre-order traversal.
        """
        if self.val is not None:
            vals.append([self.val, self.key])
        if self.left is not None:
            self.left.preorder(vals)
        if self.right is not None:
            self.right.preorder(vals)
        return vals

    def inorder(self, vals):
        """
        In-order traversal of the BST.

        Parameters
        ----------
        vals : list
            A list to store values during traversal.

        Returns
        -------
        list
            List of values in in-order traversal.
        """
        if self.left is not None:
            self.left.inorder(vals)
        if self.val is not None:
            vals.append([self.val, self.key])
        if self.right is not None:
            self.right.inorder(vals)
        return vals

    def postorder(self, vals):
        """
        Post-order traversal of the BST.

        Parameters
        ----------
        vals : list
            A list to store values during traversal.

        Returns
        -------
        list
            List of values in post-order traversal.
        """
        if self.left is not None:
            self.left.postorder(vals)
        if self.right is not None:
            self.right.postorder(vals)
        if self.val is not None:
            vals.append([self.val, self.key])
        return vals

    def toJson(self):
        """
        Convert the BST to a JSON string.

        Returns
        -------
        str
            JSON representation of the BST.
        """
        return json.dumps(self, default=lambda o: o.__dict__)


class trialCrimes:
    """
    Class for processing crime data and storing it in a BST.
    """
    @staticmethod
    def data_tree_crimes():
        """
        Read crime data from a JSON file and store it in a BST.
        The BST is then pickled for persistence.
        """
        bst = bstNode()
        data = readWriteFile.readFile("./json_files/crimes_new.json")
        

        for i in range(len(data)):
            bst.insert(
                [
                    data[i]["city name"],
                    float(data[i]["Crimes per day"]),
                    data[i]["State"],
                ],
                int(data[i]["City rank"]),
            )

        with open(f"./json_files/tree_crimes.pickle", "wb") as f:
            pickle.dump(bst, f)

    # Call the method to process the data
    data_tree_crimes()
