import json
import pickle
class BSTNode:
    def __init__(self, val=None,key = None):
        self.left = None
        self.right = None
        self.val = val
        self.key = key

    def insert(self, val,key):
        if not self.val:
            self.val = val
            self.key = key
            return

        if self.key == key:
            return

        if key < self.key:
            if self.left:
                self.left.insert(val,key)
                return
            self.left = BSTNode(val,key)
            return

        if self.right:
            self.right.insert(val,key)
            return
        self.right = BSTNode(val,key)

    def delete(self, val,key):
        if self == None:
            return self
        if val < self.val:
            if self.left:
                self.left = self.left.delete(val,key)
            return self
        if val > self.val:
            if self.right:
                self.right = self.right.delete(val,key)
            return self
        if self.right == None:
            return self.left
        if self.left == None:
            return self.right
        min_larger_node = self.right
        while min_larger_node.left:
            min_larger_node = min_larger_node.left
        self.val = min_larger_node.val
        self.right = self.right.delete(min_larger_node.val,min_larger_node.key)
        return self

    def exists(self, key):
        print('key',key)
        print('stored key',self.key)
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
        current = self
        while current.left is not None:
            current = current.left
        return current.val

    def get_max(self):
        current = self
        while current.right is not None:
            current = current.right
        return current.val

    def preorder(self, vals):
        if self.val is not None:
            vals.append([self.val,self.key])
        if self.left is not None:
            self.left.preorder(vals)
        if self.right is not None:
            self.right.preorder(vals)
        return vals

    def inorder(self, vals):
        if self.left is not None:
            self.left.inorder(vals)
        if self.val is not None:
            vals.append([self.val,self.key])
        if self.right is not None:
            self.right.inorder(vals)
        return vals

    def postorder(self, vals):
        if self.left is not None:
            self.left.postorder(vals)
        if self.right is not None:
            self.right.postorder(vals)
        if self.val is not None:
            vals.append([self.val,self.key])
        return vals
    
    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)


class crimes:

    def data_tree_crimes():
        bst = BSTNode()
        with open('crimes_new.json','r') as myfile:
            data = json.load(myfile)

        for i in range(len(data)):

            bst.insert([data[i]['city name'],float(data[i]['Crimes per day']),data[i]['State']],int(data[i]['City rank']))
       
        # with open("tree_crimes.json", 'w') as myfile:
        #     myfile.write(json.dumps(bst.toJson(),indent = 4))

        
        with open(f'tree_crimes.pickle', 'wb') as f:
            pickle.dump(bst, f)
        # with open(f'tree_crimes.pickle', 'rb') as f:
        #     crime_tree = pickle.load(f)

        # print(crime_tree.preorder([]))
    data_tree_crimes()


  
