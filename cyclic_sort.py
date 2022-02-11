# Problem Statement #
# We are given an array containing ‘n’ distinct numbers taken from the range 0 to ‘n’. Since the array has only ‘n’ numbers out of the total ‘n+1’ numbers, find the missing number.

# Example 1:

# Input: [4, 0, 3, 1]
# Output: 2
# Example 2:

# Input: [8, 3, 5, 2, 4, 6, 0, 1]
# Output: 7

def find_missing_number(nums):
  j = 0
  #cyclic sort first
  while j < len(nums):
    i = nums[j]
    if j != nums[j] and i < len(nums):
      nums[j], nums[i] = nums[i], nums[j]
    else:
      j += 1
  print(nums)
  #find missing
  for i,val in enumerate(nums):   
    if i != val:
      return i
  return -1

def main():
  print(find_missing_number([4, 0, 3, 1]))
  print(find_missing_number([8, 3, 5, 2, 4, 6, 0, 1]))


main()