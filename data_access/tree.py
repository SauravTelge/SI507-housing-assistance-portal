import json

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

        if self.val == val:
            return

        if val < self.val:
            if self.left:
                self.left.insert(val,key)
                return
            self.left = BSTNode(val,key)
            return

        if self.right:
            self.right.insert(val,key)
            return
        self.right = BSTNode(val,key)

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

    def exists(self, val,key):
        if val == self.val:
            return True

        if val < self.val:
            if self.left == None:
                return False
            return self.left.exists(val,key)

        if self.right == None:
            return False
        return self.right.exists(val,key)

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



class University():
    def __init__(self)-> None:
        self.university_name = None
        self.city = None
        self.overall_rank = None

    def display(self,univ,city):
        with open('universities.json','r') as myfile:  
            data = json.load(myfile)  
            print(data)

        return (self.university_name,self.city,self.overall_rank)
    


class crimes(University):
    def __init__(self) -> None:

        # super.__init__()

        self.city_name = None
        self.city_crime_rate_rank = None
        self.state = None
        self.crime_rate_per_day = None

    def data_tree_crimes():
        bst = BSTNode()
        with open('crimes.json','r') as myfile:  
            data = json.load(myfile)

        for i in range(len(data)):

            bst.insert(int(data[i]['City rank']),data[i]['city name'])

    data_tree_crimes()

# class Weather():
#     def __init__(self) -> None:
        

class Housing():
    def __init__(self) -> None:
        # super.__init__()
        self.rent = None
        self.utilities = None
        self.transportation = None
        self.restaurant = None

    def data_tree():
        print('here')
        with open('housing.json','r') as myfile:  
            data = json.load(myfile)  
  
