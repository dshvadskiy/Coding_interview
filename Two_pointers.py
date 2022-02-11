# Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target.

# Write a function to return the indices of the two numbers (i.e. the pair) such that they add up to the given target.

# Example 1:

# Input: [1, 2, 3, 4, 6], target=6
# Output: [1, 3]
# Explanation: The numbers at index 1 and 3 add up to 6: 2+4=6
# Example 2:

# Input: [2, 5, 9, 11], target=11
# Output: [0, 2]
# Explanation: The numbers at index 0 and 2 add up to 11: 2+9=11


def pair_with_targetsum(arr, target_sum):
  # TODO: Write your code here
  start = 0
  end = len(arr) -1
  while start < end:
    if arr[start] + arr[end] > target_sum:
      end -= 1
    elif arr[start] + arr[end] < target_sum:
      start += 1
    else:
      return [start,end]
  return [-1, -1]
#print(pair_with_targetsum([2, 5, 9, 11], 11))

########################

# Given an array of sorted numbers, remove all duplicates from it. You should not use any extra space; after removing the duplicates in-place return the length of the subarray that has no duplicate in it.

# Example 1:

# Input: [2, 3, 3, 3, 6, 9, 9]
# Output: 4
# Explanation: The first four elements after removing the duplicates will be [2, 3, 6, 9].
# Example 2:

# Input: [2, 2, 2, 11]
# Output: 2
# Explanation: The first two elements after removing the duplicates will be [2, 11].

def remove_duplicates(arr):
  # TODO: Write your code here
  start = 0 
  end =1
  length = 1
  while end < len(arr):
    if arr[start] != arr[end]:
      length += 1
      start = end
    end += 1
  return length
print(remove_duplicates([2, 2, 2, 11]))


########################
# Given an array with positive numbers and a positive target number, find all of its contiguous subarrays whose product is less than the target number.

# Example 1:

# Input: [2, 5, 3, 10], target=30 
# Output: [2], [5], [2, 5], [3], [5, 3], [10]
# Explanation: There are six contiguous subarrays whose product is less than the target.
# Example 2:

# Input: [8, 2, 6, 5], target=50 
# Output: [8], [2], [8, 2], [6], [2, 6], [5], [6, 5] 
# Explanation: There are seven contiguous subarrays whose product is less than the target.

def find_subarrays(arr, target):
  result = []
  start = 0
  end = 0
  prod = arr[0]
  while start < len(arr):
    while end < len(arr):
      if end > start:
        prod *= arr[end] 
      #if product(arr[start:end+ 1]) < target:
      if prod < target:
        print(start, end, arr[start:end+1])
        result.append(arr[start:end+1])
      else:
        break
      end += 1
    start += 1
    end = start
    if start < len(arr):
      prod = arr[start]  

  # TODO: Write your code here
  return result

def product(arr):
  result = 1
  for elem in arr:
    result = result * elem
  return result

############################################

# Given two strings containing backspaces (identified by the character ‘#’), check if the two strings are equal.

# Example 1:

# Input: str1="xy#z", str2="xzz#"
# Output: true
# Explanation: After applying backspaces the strings become "xz" and "xz" respectively.
# Example 2:

# Input: str1="xy#z", str2="xyz#"
# Output: false
# Explanation: After applying backspaces the strings become "xz" and "xy" respectively.
# Example 3:

# Input: str1="xp#", str2="xyz##"
# Output: true
# Explanation: After applying backspaces the strings become "x" and "x" respectively.
# In "xyz##", the first '#' removes the character 'z' and the second '#' removes the character 'y'.
# Example 4:

# Input: str1="xywrrmp", str2="xywrrmu#p"
# Output: true
# Explanation: After applying backspaces the strings become "xywrrmp" and "xywrrmp" respectively.

def backspace_compare(str1, str2):
  # TODO: Write your code here
  print(str1,str2)
  str1 = remove_backspaces(str1)
  str2 = remove_backspaces(str2)
  print(str1, str2)
  return str1 == str2

def remove_backspaces(str_s):
  str1 = list(str_s)
  #print(str1)
  start = 0
  insert = 0
  while start < len(str1):
    str1[insert] = str1[start]
    if str1[start] == '#':
        insert -= 1
    else:
      insert += 1
    start +=1
      
    #print(insert,start)  
  return ''.join(str1[:insert])


def main():
  # print(find_subarrays([2, 5, 3, 10], 30))
  # print(find_subarrays([8, 2, 6, 5], 50))

  print(backspace_compare('xy#z', 'xzz#'))
  print(backspace_compare('xy#z', 'xyz#'))
  print(backspace_compare('xp#', 'xyz##'))
  print(backspace_compare('xywrrmp', 'xywrrmu#p'))

main()
