from collections import deque
class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def find_level_averages(root):
    result = []
    # TODO: Write your code here
    queue = deque()
    queue.append(root)
    while len(queue) > 0:
        level_sum =0
        level_size = len(queue)
        for _ in range(level_size):
            node = queue.popleft()
            level_sum += node.val
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level_sum/level_size)
    return result

def find_minimum_depth(root):
    if root is None:
        return 0
    queue = deque()
    queue.append(root)
    depth = 0
    while len(queue) > 0:
        depth += 1
        levelSize = len(queue)
        for _ in range(levelSize):
            node = queue.popleft()
            if node.left is None and node.right is None:
                return depth
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
    return depth

def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Tree Minimum Depth: " + str(find_minimum_depth(root)))
  root.left.left = TreeNode(9)
  root.right.left.left = TreeNode(11)
  print("Tree Minimum Depth: " + str(find_minimum_depth(root)))
# def main():
#   root = TreeNode(12)
#   root.left = TreeNode(7)
#   root.right = TreeNode(1)
#   root.left.left = TreeNode(9)
#   root.left.right = TreeNode(2)
#   root.right.left = TreeNode(10)
#   root.right.right = TreeNode(5)
#   print("Level averages are: " + str(find_level_averages(root)))



main()