#Problem 1: Given the head of a LinkedList with a cycle, find the length of the cycle.

class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next


def find_cycle_length(head):
  slow, fast = head, head
  while fast is not None and fast.next is not None:
    fast = fast.next.next
    slow = slow.next
    if slow == fast:  # found the cycle
      return calculate_cycle_length(slow)

  return 0


def calculate_cycle_length(slow):
  current = slow
  cycle_length = 0
  while True:
    current = current.next
    cycle_length += 1
    if current == slow:
      break
  return cycle_length


# def main():
#   head = Node(1)
#   head.next = Node(2)
#   head.next.next = Node(3)
#   head.next.next.next = Node(4)
#   head.next.next.next.next = Node(5)
#   head.next.next.next.next.next = Node(6)
#   head.next.next.next.next.next.next = head.next.next
#   print("LinkedList cycle length: " + str(find_cycle_length(head)))

#   head.next.next.next.next.next.next = head.next.next.next
#   print("LinkedList cycle length: " + str(find_cycle_length(head)))


# main()

#######################################

#Given the head of a Singly LinkedList that contains a cycle, write a function to find the starting node of the cycle.

#from __future__ import print_function


class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

  def print_list(self):
    temp = self
    while temp is not None:
      print(temp.value, end='')
      temp = temp.next
    print()


def find_cycle_start(head):
  slow = head
  fast = head
  while fast.next.next: 
    slow = slow.next
    fast = fast.next.next
    if slow == fast:
      cycle_len = find_cycle_len(slow)
      return find_start(head, cycle_len)
  return head

def find_cycle_len(slow):
  length = 1
  start = slow
  while slow.next != start:
    slow = slow.next
    length += 1
  return length

def find_start(head, cycle_length):
  pointer1 = head
  pointer2 = head
  # move pointer2 ahead 'cycle_length' nodes
  while cycle_length > 0:
    pointer2 = pointer2.next
    cycle_length -= 1
  # increment both pointers until they meet at the start of the cycle
  while pointer1 != pointer2:
    pointer1 = pointer1.next
    pointer2 = pointer2.next
  return pointer1


# def main():
#   head = Node(1)
#   head.next = Node(2)
#   head.next.next = Node(3)
#   head.next.next.next = Node(4)
#   head.next.next.next.next = Node(5)
#   head.next.next.next.next.next = Node(6)

#   head.next.next.next.next.next.next = head.next.next
#   print("LinkedList cycle start: " + str(find_cycle_start(head).value))

#   head.next.next.next.next.next.next = head.next.next.next
#   print("LinkedList cycle start: " + str(find_cycle_start(head).value))

#   head.next.next.next.next.next.next = head
#   print("LinkedList cycle start: " + str(find_cycle_start(head).value))


# main()


######################################
# Problem Statement#
# Given the head of a Singly LinkedList, write a method to return the middle node of the LinkedList.

# If the total number of nodes in the LinkedList is even, return the second middle node.

# Example 1:

# Input: 1 -> 2 -> 3 -> 4 -> 5 -> null
# Output: 3
# Example 2:

# Input: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> null
# Output: 4
# Example 3:

# Input: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> null
# Output: 4


class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next


def find_middle_of_linked_list(head):
  # TODO: Write your code here
  #return headgma
  fast = head
  slow = head

  while (fast is not None and fast.next is not None):
    slow = slow.next
    fast = fast.next.next
  return slow



def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)

  print("Middle Node: " + str(find_middle_of_linked_list(head).value))

  head.next.next.next.next.next = Node(6)
  print("Middle Node: " + str(find_middle_of_linked_list(head).value))

  head.next.next.next.next.next.next = Node(7)
  print("Middle Node: " + str(find_middle_of_linked_list(head).value))


main()
