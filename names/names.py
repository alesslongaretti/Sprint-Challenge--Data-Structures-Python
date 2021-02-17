import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

        # Insert the given value into the tree
    def insert(self, value):
        # if new value is >= the current node value, Go right.
        if value >= self.value:
            # if there is no node there
            if self.right is None:
                # create new node
                self.right = BSTNode(value)
            # (there is a BSTNode to the right), recurse (do the same thing and compare if its less than or greater than)
            else:
                # insert value to self.right
                self.right.insert(value)
        # if new value is < the current node value, Go left.
        if value < self.value:
            # if there is no node to the left
            if self.left is None:
                # Create new node
                self.left = BSTNode(value)
            # (there is a BSTNode to the left), recurse (do the same thing and compare if its less than or greater than)
            else:
                # insert value to self.left
                self.left.insert(value)

        # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # check if target is the first node
        if target == self.value:
            return True
        # if target is < the first node go left
        if target < self.value:
            # if there is nothing to the left return None
            if self.left is None:
                return False
            # if there is a value to the left, recurse (check if the target == self.value)
            else:
                return self.left.contains(target)
        # if target is > self.value, go right
        if target > self.value:
            # if there is nothing to the right return False
            if self.right is None:
                return False
            # if there is a node to the right, recurse(check if the target == self.value)
            else:
                return self.right.contains(target)

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
bst = BSTNode("")

for name_1 in names_1:
    bst.insert(name_1)
for name_2 in names_2:
    if bst.contains(name_2):
        duplicates.append(name_2)



# RUNTIME O(n^2)

# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
