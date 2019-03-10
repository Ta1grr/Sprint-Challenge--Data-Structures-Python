import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def breadth_first_for_each(self, cb):

        # To keep track of numbers
        queue = []

        output = []

        # Assigning current to the class node itself
        current = self

        # Append the first value into the queue [5], []
        queue.append(current.value)

        while len(queue) > 0:
            # Compare the instance of BinarySearchTree class value attribute to the first index
            # of queue.
            if current.value == queue[0]:
                # If it is true, then we check both "current" left and right child nodes to be not None
                # and then append them to queue.
                if current.left is not None:
                    queue.append(current.left.value)
                if current.right is not None:
                    queue.append(current.right.value)
                # From here, I call the anonymous function "cb" with the current value
                output.append(queue[0])
                # Finally pop the first value of the list of queue
                queue.pop(0)
            else:
                # If Line 61 is false, then I check if the first index of Queue to be less than or
                # greater than of the current.value (Note: this will work on ordinary binary trees except for heaps)
                if queue[0] < current.value:
                    # If there's no left node, then it'll reassign current back to self so it can start back at root.
                    if not current.left:
                        current = self
                    # Else, reassign current to the its left child node.
                    else:
                        current = current.left
                else:
                    # If there's no right node, then it'll reassign current back to self so it can start back at root.
                    if not current.right:
                        current = self
                    # Else, reassign current to the its left child node.
                    else:
                        current = current.right
        return output


    def insert(self, value):
        new_tree = BinarySearchTree(value)
        if self.value  == None:
            self.value = new_tree

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

# -- My Code --
# The time complexity of my code is O(n log n) first iteration of names_1 is N
# while bst2 contains is logn so it equates to 0(n log n)
# runtime: 0.19114184379577637 seconds
# Initialize duplicate to be a list
duplicates = []

# Assigning self.value to be the first index of names_2 list
bst2 = BinarySearchTree(names_2[0])

# Iterating through names_2 and assigning each index to a node based on root
for name_2 in range(len(names_2) - 1):
    bst2.insert(names_2[name_2])

# Iterating through names_1 and calling the contains method to search through the bst2(names_2) tree 
# for matching names to names_1. If true, then append name_1 to duplicates
for name_1 in names_1:
    if bst2.contains(name_1):
        duplicates.append(name_1)
        
# -- Original Code --        
# The time complexity of this code is N**2, because iteration of the index names_1 is one whole iteration of name_2.
# runtime: 6.769580125808716 seconds
duplicates = []
for name_1 in names_1:
    for name_2 in names_2:
        if name_1 == name_2:
            duplicates.append(name_1)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

