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
    
    #Level Order Traversal

    def levelOrderTraversal(self):
        root=self.root
        if root is None:
            return 

        queue=[]
        queue.append(root)
        queue.append(None)

        while(queue):
            
            node=queue.pop(0)
            if node is None:
                print()
                if queue:
                    queue.append(None)
            else:
                print(node.data, end=" ")
                if node.left is not None:
                    queue.append(node.left)
                
                if node.right is not None:
                    queue.append(node.right)







if __name__=="__main__":
    tree=Tree()
    tree.root=tree.buildTree(tree.root)
    tree.levelOrderTraversal()
