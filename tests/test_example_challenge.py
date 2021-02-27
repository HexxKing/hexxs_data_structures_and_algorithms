import pytest
from data_structures_and_algorithms.example_catagory.example_challenge.example_challenge import hello_world

#Test Connection 
def test_hello_world():
  greetings = hello_world()
  assert "Hello World!"
