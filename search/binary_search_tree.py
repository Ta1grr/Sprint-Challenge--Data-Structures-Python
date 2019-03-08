class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def depth_first_for_each(self, cb):
    pass    

  def breadth_first_for_each(self, cb):
    """ 
    * `breadth_first_for_each(cb)` receives a callback function as a parameter. 
    It should then execute the anonymous function on each node in the tree 
    in [breadth-first](https://en.wikipedia.org/wiki/Breadth-first_search) order. 
    Your task is to implement the logic to traverse the tree in left-to-right breadth-first fashion.
   
    * Remember that the anonymous function is supplied by the caller of the method. 
    All you have to do is ensure that the anonymous function is being called on each 
    tree node in the desired order.
   
     _HINT_: In order to achieve breadth-first order, you'll probably want to utilize a Queue data structure.

    * Run `python test_breadth_first_search.py` to test your breadth-first search implementation.
    """
    # To keep track of numbers
    Queue = []

    # If I input [3, 8, 4, 9, ]



  def insert(self, value):
    new_tree = BinarySearchTree(value)
    if (value < self.value):
      if not self.left:
        self.left = new_tree
      else:
        self.left.insert(value)
    elif value >= self.value:
      if not self.right:
        self.right = new_tree
      else:
        self.right.insert(value)

  def contains(self, target):
    if self.value == target:
      return True
    if target < self.value:
      if not self.left:
        return False
      else:
        return self.left.contains(target)
    else:
      if not self.right:
        return False
      else:
        return self.right.contains(target)

  def get_max(self):
    if not self:
      return None
    max_value = self.value
    current = self
    while current:
      if current.value > max_value:
        max_value = current.value
      current = current.right
    return max_value
