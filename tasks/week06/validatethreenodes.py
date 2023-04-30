import pytest
from binarysearchtree import *

def validateThreeNodes(bst, valueOne, valueTwo, valueThree):
    """
    Checks if the given three nodes have the required relationship in the Binary Search Tree.
    
    This function validates if either nodeTwo is a descendant of nodeOne and nodeThree is a descendant
    of nodeTwo, or if nodeOne is a descendant of nodeTwo and nodeThree is an ascendant of nodeTwo.

    Parameters:
    bst (BST): he Binary Search Tree containing the nodes.
    valueOne (int): The value of the first node.
    valueTwo (int): The value of the second node.
    valueThree (int): The value of the third node.

    Returns:
    bool: True if the given nodes have the required relationship, False otherwise.
    """
    # Write your code here.

    if not valueOne or not valueTwo or not valueThree:
        return False
    
    def is_descendant(child_value, parent_value):
        if child_value == parent_value:
            return True
        
        current_node = bst.root
        while current_node:
            if current_node.value == parent_value:
                break
            
            if child_value < current_node.value:
                current_node = current_node.left_child
            else:
                current_node = current_node.right_child
                
        if not current_node:
            return False
        
        #return bst._contains(child_value, current_node)
        return bst._contains(current_node, child_value)
    
    def is_ascendant(parent_value, child_value):
        return is_descendant(child_value, parent_value)
    
    #print("Node two is descendant of node one: ", is_descendant(valueTwo, valueOne))
    #print("Node three is descendant of node two: ", is_descendant(valueThree, valueTwo))
    
    first_case = False
    second_case = False
    if is_descendant(valueTwo, valueOne) and is_descendant(valueThree, valueTwo):
        first_case = True
    
    #print("Node one is descendant of node two: ", is_descendant(valueOne, valueTwo))
    #print("Node three is ascendant of node two: ", is_ascendant(valueThree, valueTwo))
    if is_descendant(valueOne, valueTwo) and is_ascendant(valueThree, valueTwo):
        second_case = True
    
    #print("First case: ", first_case)
    #print("Second case: ", second_case)
    if first_case or second_case:
        return True
    
    return False


@pytest.fixture(scope="session")
def data():
    
    array = [[5, 2, 1, 0, 4, 3, 7, 6, 8],
             [5, 3, 2, 1, 0, 4, 7, 6, 8],
             [5, 3, 2, 1, 0, 4, 7, 6, 8],
             [2, 1, 3, 4, 5, 6, 7, 8, 9],
             [6, 4, 3, 1, 2, 8, 7, 9],
             [2, 1, 3, 4],
             [8, 4, 3, 2, 1, 10, 9, 14, 12, 11, 6, 7, 13],
             [8, 7, 6, 5, 4, 3, 2, 1, 9],
             [3, 2, 1],
             [3, 2, 1],
             [6, 4, 2, 1, 3, 5, 8, 7, 9],
             [10, 6, 5, 3, 1, 2, 4, 8, 7, 9, 15, 14, 13, 11, 12, 18, 17, 16],
             [10, 6, 5, 3, 1, 2, 4, 8, 7, 9, 15, 14, 13, 11, 12, 18, 17, 16],
             [5, 3, 1, 0, 2, 4, 7, 6, 8],
             [5, 3, 1, 0, 2, 4, 7, 6, 8]]
    return array

def test_1(data):
    """
    Test evaluation for "nodeOne": "5","nodeThree": "3","nodeTwo": "2"
    """
    bst = BST()
    for value in data[0]:
      bst.add(value)
    assert validateThreeNodes(bst,5,2,3) == True

def test_2(data):
    """
    Test evaluation for "nodeOne": "5", "nodeThree": "1", "nodeTwo": "8",
    """
    bst = BST()
    for value in data[1]:
      bst.add(value)
    assert validateThreeNodes(bst,5,8,1) == False

def test_3(data):
    """
    Test evaluation for   "nodeOne": "8","nodeThree": "2","nodeTwo": "5",
    """
    bst = BST()
    for value in data[2]:
      bst.add(value)
    assert validateThreeNodes(bst,8,5,2) == False

def test_4(data):
    """
    Test evaluation for  "nodeOne": "2","nodeThree": "8","nodeTwo": "5"
    """
    bst = BST()
    for value in data[3]:
      bst.add(value)
    assert validateThreeNodes(bst,2,5,8) == True

def test_5(data):
    """
    Test evaluation for "nodeOne": "4", "nodeThree": "2", "nodeTwo": "1",
    """
    bst = BST()
    for value in data[4]:
      bst.add(value)
    assert validateThreeNodes(bst,4,1,2) == True

def test_6(data):
    """
    Test evaluation for "nodeOne": "1","nodeThree": "3","nodeTwo": "2",
    """
    bst = BST()
    for value in data[5]:
      bst.add(value)
    assert validateThreeNodes(bst,1,2,3) == False

def test_7(data):
    """
    Test evaluation for "nodeOne": "2","nodeThree": "13","nodeTwo": "4"
    """
    bst = BST()
    for value in data[6]:
      bst.add(value)
    assert validateThreeNodes(bst,2,4,13) == False

def test_8(data):
    """
    Test evaluation for "nodeOne": "8","nodeThree": "1","nodeTwo": "7"
    """
    bst = BST()
    for value in data[7]:
      bst.add(value)
    assert validateThreeNodes(bst,8,7,1) == True

def test_9(data):
    """
    Test evaluation for "nodeOne": "2","nodeThree": "3","nodeTwo": "1"
    """
    bst = BST()
    for value in data[8]:
      bst.add(value)
    assert validateThreeNodes(bst,2,1,3) == False

def test_10(data):
    """
    Test evaluation for "nodeOne": "1", "nodeThree": "3", "nodeTwo": "2"
    """
    bst = BST()
    for value in data[9]:
      bst.add(value)
    assert validateThreeNodes(bst,1,2,3) == True

def test_11(data):
    """
    Test evaluation for "nodeOne": "9","nodeThree": "6","nodeTwo": "8"
    """
    bst = BST()
    for value in data[10]:
      bst.add(value)
    assert validateThreeNodes(bst,9,8,6) == True

def test_12(data):
    """
    Test evaluation for "nodeOne": "12","nodeThree": "15","nodeTwo": "13"
    """
    bst = BST()
    for value in data[11]:
      bst.add(value)
    assert validateThreeNodes(bst,12,13,15) == True

def test_13(data):
    """
    Test evaluation for "nodeOne": "5","nodeThree": "15","nodeTwo": "10"
    """
    bst = BST()
    for value in data[12]:
      bst.add(value)
    assert validateThreeNodes(bst,5,10,15) == False

def test_14(data):
    """
    Test evaluation for "nodeOne": "5","nodeThree": "4","nodeTwo": "3"
    """
    bst = BST()
    for value in data[13]:
      bst.add(value)
    assert validateThreeNodes(bst,5,3,4) == True

def test_15(data):
    """
    Test evaluation for "nodeOne": "5","nodeThree": "1","nodeTwo": "3"
    """
    bst = BST()
    for value in data[14]:
      bst.add(value)
    assert validateThreeNodes(bst,5,3,1) == True
