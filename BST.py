class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

class BST:
  def __init__(self):
    self.root = None


  def insert(self, value):
    newNode = Node(value)
    if not self.root:
      self.root = newNode
    else:
      current = self.root
      while True:
        if current.value < value:
          if not current.right:
            current.right = newNode
            return 
          current = current.right
        else:
          if not current.left:
            current.left = newNode
            return
          current = current.left


  def breadthFirstSearch(self):
    currentNode = self.root
    results = []
    traversal = []
    traversal.append(currentNode)
    while len(traversal) > 0:
      currentNode = traversal.pop(0)
      results.append(currentNode.value)
      if currentNode.left:
        traversal.append(currentNode.left)
      if currentNode.right:
        traversal.append(currentNode.right)

    return results


  def breadthFirstSearchR(self, queue, my_list):
    if not queue:
      return my_list
    
    currentNode = queue.pop(0)
    my_list.append(currentNode.value)
    if currentNode.left:
      queue.append(currentNode.left)
    if currentNode.right:
      queue.append(currentNode.right)

    return self.breadthFirstSearchR(queue, my_list)


  def inOrderTraversal(self):
    res = []
    root = self.root
    self.helper1(root, res)
    return res

  def helper1(self, root, res):
    if root:
      self.helper1(root.left, res)
      res.append(root.value)
      self.helper1(root.right, res)


  def preOrderTraversal(self):
    res = []
    root = self.root
    self.helper2(root, res)
    return res

  def helper2(self, root, res):
    if root:
      res.append(root.value)
      self.helper2(root.left, res)
      self.helper2(root.right, res)
    
  
  def postOrderTraversal(self):
    res = []
    root = self.root
    self.helper3(root, res)
    return res

  def helper3(self, root, res):
    if root:
      self.helper3(root.left, res)
      self.helper3(root.right, res)
      res.append(root.value)



myBST = BST()
myBST.insert(13)
myBST.insert(4)
myBST.insert(40)
myBST.insert(23)
myBST.insert(50)
myBST.breadthFirstSearch()
print(myBST.breadthFirstSearch())
# print(myBST.breadthFirstSearchR([myBST.root], []))
# print(myBST.root.right.right.value)
print(myBST.inOrderTraversal())
print(myBST.preOrderTraversal())
print(myBST.postOrderTraversal())
