import pytest
from data_structures_and_algorithms.example_catagory.example_challenge.example_challenge import hello_world

#Test Connection 
def test_hello_world():
  greetings = hello_world()
  assert "Hello World!"
  
# “Happy Path” - Expected outcome

# Test One 

# Test Some

# Test Many

# Test Repetition

# Expected failure

# Edge Case 

# =====Tree Specific Tests=====
# Can successfully instantiate an empty tree
# Can successfully instantiate a tree with a single root node
# Can successfully add a left child and right child to a single root node
# Can successfully return a collection from a preorder traversal
# Can successfully return a collection from an inorder traversal
# Can successfully return a collection from a postorder traversal