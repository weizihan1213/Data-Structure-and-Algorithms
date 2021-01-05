class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class myStack:
  def __init__(self):
    self.top = None
    self.bottom = None
    self.length = 0


  def peek(self):
    if self.top:
      return self.top
    print('There\'s no element in the Stack')


  def push(self, data):
    newNode = Node(data)
    if self.bottom:
      current = self.top
      self.top = newNode
      self.top.next = current
    else:
      self.bottom = self.top = newNode
    self.length += 1
    return self


  def pop(self):
    if self.top:
      current = self.top
      self.top = current.next
      self.length -= 1
      return self.top
    print('There\'s no element in the Stack')


  def printStack(self):
    current = self.top
    values = []
    while current != None:
      values.append(current.data)
      current = current.next
    print(values)

s1 = myStack()
s1.push(10)
s1.push(5)
s1.push(20)
s1.printStack()
s1.pop()
s1.printStack()