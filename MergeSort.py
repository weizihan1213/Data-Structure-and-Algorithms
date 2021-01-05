numbers = [13, 2, 67, 45, 3, 9]

def mergeSort(numbers):
  if len(numbers) > 1:
    left = numbers[:len(numbers)//2]
    right = numbers[len(numbers)//2:]

    mergeSort(left)
    mergeSort(right)


    i = 0
    j = 0
    k = 0

    while i < len(left) and j < len(right):
      if left[i] < right[j]:
        numbers[k] = left[i]
        i += 1
      else:
        numbers[k] = right[j]
        j += 1
      
      k += 1

    while i < len(left):
      numbers[k] = left[i]
      i += 1
      k += 1
    
    while j < len(right):
      numbers[k] = right[j]
      j += 1
      k += 1

    return numbers

print(mergeSort(numbers))