numbers = [3, 5, 2, -1, 0, 7, 46]

def selection(num = []):
  for i in range(len(numbers)):
    min_idx = i
    for j in range(i+1, len(numbers)):
      if num[min_idx] > num[j]:
        min_idx = j

    num[min_idx], num[i] = num[i], num[min_idx]

  return num

print(selection(numbers))