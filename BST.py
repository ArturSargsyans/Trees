class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

class BST:
    def __init__(self):
        self.root = None

    def __str__(self):
        if self.root == None:
            return "empty"
        else:
            return str(self.root.data)

    def addNode(self, node):
        if self.root == None:
            self.root = node
        else:
            self.addToCorrectParent(node, self.root)

    def addToCorrectParent(self, node, curr_root):

        if node.data < curr_root.data:
            if curr_root.left == None:
                curr_root.left = node
            else:
                self.addToCorrectParent(node, curr_root.left)
        elif node.data > curr_root.data:
            if curr_root.right == None:
                curr_root.right = node
            else:
                self.addToCorrectParent(node,curr_root.right)

        else:
            print("value has been skipped")
            pass

    def PreorderList(self, currentroot, list):
        if currentroot != None:
            list.append(currentroot.data)
            list = self.PreorderList(currentroot.left, list)
            list = self.PreorderList(currentroot.right, list)
        return list

    def PreorderPrint(self):
        print(self.PreorderList(self.root, []))

def main():
    myBST = BST()

    Node1 = Node(50)
    Node2 = Node(20)
    Node3 = Node(3)
    Node4 = Node(34)
    Node5 = Node(7)
    Node6 = Node(99)
    Node7 = Node(25)
    Node8 = Node(6)
    myBST.addNode(Node1)
    myBST.addNode(Node2)
    myBST.addNode(Node3)
    myBST.addNode(Node4)
    myBST.addNode(Node5)
    myBST.addNode(Node6)
    myBST.addNode(Node7)
    myBST.addNode(Node8)


    myBST.PreorderPrint()



main()