class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    

class Tree:
    def __init__(self):
        self.root=None

    def buildTree(self,root):
        print("Enter the data")
        data=int(input())

        if data==-1:
            return None

        root=Node(data)
        self.root=Node(data)

        print("Enter the data inserting in left of",data)
        root.left=self.buildTree(root.left)

        print("Enter the data inserting in right of",data)
        root.right=self.buildTree(root.right)

        return root





if __name__=="__main__":
    tree=Tree()
    tree.root=tree.buildTree(tree.root)
