#Given a binary tree and a number ‘S’, find all paths from root-to-leaf such that the sum of all
#  the node values of each path equals ‘S’.
class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def find_paths(root, sum):
  all_paths = []
  current_path = []
  find_path(root, sum, current_path, all_paths)
  
  return all_paths

def find_path(root,sum, current_path, all_paths):
  if root == None:
    return
  current_path.append(root.val)  
  if sum == root.val and root.left == None and root.right == None:
    all_paths.append(list(current_path))
  if root.left != None:
    find_path(root.left, sum - root.val, current_path, all_paths)
  if root.right != None:
    find_path(root.right, sum - root.val,current_path, all_paths)
  del current_path[-1]

# def main():

#   root = TreeNode(12)
#   root.left = TreeNode(7)
#   root.right = TreeNode(1)
#   root.left.left = TreeNode(4)
#   root.right.left = TreeNode(10)
#   root.right.right = TreeNode(5)
#   sum = 23
#   print("Tree paths with sum " + str(sum) +
#         ": " + str(find_paths(root, sum)))


# main()
############################

#Given a binary tree where each node can only have a digit (0-9) value, each root-to-leaf path will 
# represent a number. Find the total sum of all the numbers represented by all paths.
class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def find_sum_of_path_numbers(root):
  # TODO: Write your code here
  sum = 0
  sum = iterate_tree(root, sum)
  return sum

def iterate_tree(current_node, sum):
  if current_node == None:
    return 0
  sum = 10 * sum + current_node.val

  if current_node.left is None and current_node.right is None:
    return sum
 
  return iterate_tree(current_node.left, sum) + iterate_tree(current_node.right, sum)
  




def main():
  root = TreeNode(1)
  root.left = TreeNode(0)
  root.right = TreeNode(1)
  root.left.left = TreeNode(1)
  root.right.left = TreeNode(6)
  root.right.right = TreeNode(5)
  print("Total Sum of Path Numbers: " + str(find_sum_of_path_numbers(root)))


main()

