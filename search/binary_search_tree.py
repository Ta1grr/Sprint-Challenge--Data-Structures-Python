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
    # Assigning the value to another variable
    current = self.value

    # If I input [5, 3, 10, 4, 9, 11] with 5 to be the starting value
    #
    #            5[0]
    #           /   \
    #        3[1]   10[2]
    #       /       /   \
    #    4[3]    9[4]   11[5]
    #                         
    #
    # Step 1: [5] , []
    # Step 2: [3, 10] , [5]
    # Step 3: [10, 4], [5, 3]
    # Step 4: [4, 9, 11], [5, 3, 10]
    # Step 5: [9, 11], [5, 3, 10, 4]
    # Step 6: [11], [5, 3, 10, 4, 9]
    # Step 7: [], [5, 3, 10, 4, 9, 11]

    # Compare the parent node with the number we're searching for
    # Compare parent then add in child, starting from left to right, gotta check to make sure child is there
    # Optional I can use a while loop and just iterate until value equal cb

    # Step 1: append the first value into the queue [5], []
    if self.value is None or not Queue:
        return
    else:
        Queue.append(current)
    # Step 2: Compare the first index to what we're searching for, it it is true, return the value, if it is
    #         false then we'll add in both child nodes. i + 1 left, i + 2 right for arrays, but we can just
    #         check self.left and self.right inside classes
        if current == cb:
            return Queue[0]            
    # Step 3: If it doesn't match, remove the current node from Queue [], [5]            
        Queue.remove(current)
    # Step 4: append the left child [3], [5]
        Queue.append(self.left)
    # Step 5: append the right child [3, 10], [5]
        Queue.append(self.right)
    # Step 6: Check left side first and repeat from step 2 down to 5 until we find the value or return None
        if self.left == Queue[0]:
            self.current = self.left
            # Remove duplicates from Queue
            Queue.remove(self.left)
            return self.breadth_first_for_each(cb)
                
        elif self.right == Queue[0]:
            self.current = self.right
            Queue.remove(self.right)
            return self.breadth_first_for_each(cb)


    # # Step 1: append the first value into the queue [5], []
    # if self.value is not None:

    #     else:
    #         Queue.append(current)
    # # Step 2: Compare the first index to what we're searching for, it it is true, return the value, if it is
    # #         false then we'll add in both child nodes. i + 1 left, i + 2 right for arrays, but we can just
    # #         check self.left and self.right inside classes
    #         if current == cb:
    #             return Queue[0]            
    # # Step 3: If it doesn't match, remove the current node from Queue [], [5]            
    #         Queue.remove(current)
    # # Step 4: append the left child [3], [5]
    #         Queue.append(self.left)
    # # Step 5: append the right child [3, 10], [5]
    #         Queue.append(self.right)
    # # Step 6: Check left side first and repeat from step 2 down to 5 until we find the value or return None
    #         if self.left == Queue[0]:
    #             self.current = self.left
    #             # Remove duplicates from Queue
    #             Queue.remove(self.left)
    #             return self.breadth_first_for_each(cb)
                
    #         elif self.right == Queue[0]:
    #             self.current = self.right
    #             Queue.remove(self.right)
    #             return self.breadth_first_for_each(cb)


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
