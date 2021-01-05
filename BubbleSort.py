numbers = [45, 3, 2, 1, 6, 9, 40]

def bubbleSort(nums = []):
  has_swapped = True

  while(has_swapped):
    has_swapped = False
    for i in range(len(nums) - 1):
      if nums[i] > nums[i + 1]:
        nums[i], nums[i+1] = nums[i+1], nums[i]
        has_swapped = True

  return nums
print(bubbleSort(numbers))