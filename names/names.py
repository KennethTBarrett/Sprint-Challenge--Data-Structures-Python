import time
from binary_search_tree import BSTNode

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()


# Lambda's Code to Optimize #
# duplicates = []  # Return the list of duplicates in this data structure
# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)
# ANSWER #
# This takes approximately 5.9 seconds to run.
# Runtime complexity: O(n^2) (Quadratic) - This is called a bubble search. (?)


# BST Method - UNCOMMENT THE FOLLOWING BLOCK #
duplicates = []
BSTNode = BSTNode(names_1[0])  # Root as index 0.
for name in names_1:
    BSTNode.insert(name)  # Insert our names.
for name in names_2:
    if BSTNode.contains(name):  # If it's already there...
        duplicates.append(name)  # Append.
# This takes approximately 0.126 seconds - an efficient approach.

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to
# this problem. What's the best time you can accomplish?  Thare are no
# restrictions on techniques or data structures, but you may not import
# any additional libraries that youdid not write yourself.

# Stretch Goal Solution - UNCOMMENT THE FOLLOWING LINE #
# duplicates = set(names_1) & set(names_2)
# This took just over 0.004 seconds - using the set() datatype is
# HIGHLY efficient for this task.

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")
