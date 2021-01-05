numbers = [3, 5, 2, -1, 0, 7, 46]

def insertion(num):
  
  for i in range(1, len(num)):
    currentValue = num[i]
    currentIdx = i

    while currentIdx > 0 and num[currentIdx - 1] > currentValue:
      num[currentIdx] = num[currentIdx - 1]
      currentIdx = currentIdx - 1

    num[currentIdx] = currentValue
  
  return num


print(insertion(numbers))