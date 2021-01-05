class Node:
  def __init__(self, data = None, next = None):
    self.data = data
    self.next = next
  
class myLinkedList:
  def __init__(self):
    self.head = None


  def append(self, number):
    newNode = Node(number)
    if(self.head):
      current = self.head
      while(current.next):
        current = current.next
      current.next = newNode
    else:
      self.head = newNode


  def prepend(self, number):
    newNode = Node(number)
    if(self.head):
      newNode.next = self.head
      self.head = newNode
    else:
      self.head = newNode


  def insertAfter(self, prev_node, new_node):
    new_node = Node(new_node)
    prev_node = Node(prev_node)
    
    current = self.head
    while(current.next):
      if current.data == prev_node.data:
        new_node.next = current.next
        current.next = new_node
        return 
      current = current.next
    
    print('The given node isn\'t in the linked list')
    return 


  def printList(self):
    nodes = []
    current = self.head
    while(current != None):
      nodes.append(current.data)
      current = current.next
    print(nodes)


  def insert(self, index, value):
    newNode = Node(value)
    current = self.head
    cursor = 0
    if(index == 0):
      self.prepend(value)
    else:
      while(current != None):
        if(cursor == index - 1):
          newNode.next = current.next
          current.next = newNode
          return
        cursor += 1
        current = current.next
      print('Index out of range')

  
  def remove(self, value):
    current = self.head
    while(current.next):
      if current.next.data == value:
        current.next = current.next.next
        return self.printList()
      current = current.next


ll1 = myLinkedList()
ll1.append(5)
ll1.append(10)
ll1.append(15)
ll1.prepend(20)
ll1.insertAfter(20, 100)
ll1.insert(0, 2000)
ll1.insert(6, 600)
ll1.printList()
ll1.remove(5)
# print(ll1.head.next.data)
