
import pytest
from linkedlist import *

def removeDuplicatesFromLinkedList(linkedList):
    """
    Modify the input doubly linked list in place to remove all nodes with duplicate values.
    The modified linked list should still have its nodes sorted with respect to their values.
  
    Args:
    linkedList (LinkedList): The sorted doubly linked list from which duplicate nodes will be removed.

    Returns:
        LinkedList: The modified linked list with duplicate nodes removed.
    """
    # Initialize a new linked list
    new_linked_list = LinkedList()
    
    # Iterate over the linked list
    for value in linkedList:
        
        # If the new linked list is empty, add the first value
        if len(new_linked_list) == 0:
            new_linked_list.append(value)
        
        # If the value is not equal to the last value in the new linked list, add it
        elif value != new_linked_list.tail.data:
            new_linked_list.append(value)
    
    return new_linked_list

@pytest.fixture(scope="session")
def data():
    
    array = []
    
    # test 1 data
    array.append([1,1,1,3,4,4,4,5,6,6])

    # test 2 data
    array.append([1,1,1,1,1,4,4,5,6,6])

    # test 3 data
    array.append([1,1,1,1,1,1,1])

    # test 4 data
    array.append([1,9,11,15,15,16,17])

    # test 5 data
    array.append([1])

    # test 6 data
    array.append([-5,-1,-1,-1,5,5,5,8,8,9,10,11,11])

    # test 7 data
    array.append([1,2,3,4,5,6,7,8,9,10,11,12,12])
    
    return array

def test_1(data):
    """
    Test evaluation for [1,1,1,3,4,4,4,5,6,6] 
    """
    linkedlist = LinkedList()
    for item in data[0]:
      linkedlist.append(item)

    linkedlist_test = LinkedList()
    for item in [1,3,4,5,6]:
      linkedlist_test.append(item)

    assert removeDuplicatesFromLinkedList(linkedlist) == linkedlist_test


def test_2(data):
    """
    Test evaluation for [1,1,1,1,1,4,4,5,6,6] 
    """
    linkedlist = LinkedList()
    for item in data[1]:
      linkedlist.append(item)

    linkedlist_test = LinkedList()
    for item in [1,4,5,6]:
      linkedlist_test.append(item)

    assert removeDuplicatesFromLinkedList(linkedlist) == linkedlist_test

def test_3(data):
    """
    Test evaluation for [1,1,1,1,1,1,1] 
    """
    linkedlist = LinkedList()
    for item in data[2]:
      linkedlist.append(item)

    linkedlist_test = LinkedList()
    for item in [1]:
      linkedlist_test.append(item)

    assert removeDuplicatesFromLinkedList(linkedlist) == linkedlist_test

def test_4(data):
    """
    Test evaluation for [1,9,11,15,15,16,17] 
    """
    linkedlist = LinkedList()
    for item in data[3]:
      linkedlist.append(item)

    linkedlist_test = LinkedList()
    for item in [1,9,11,15,16,17]:
      linkedlist_test.append(item)

    assert removeDuplicatesFromLinkedList(linkedlist) == linkedlist_test

def test_5(data):
    """
    Test evaluation for [1] 
    """
    linkedlist = LinkedList()
    for item in data[4]:
      linkedlist.append(item)

    linkedlist_test = LinkedList()
    for item in [1]:
      linkedlist_test.append(item)

    assert removeDuplicatesFromLinkedList(linkedlist) == linkedlist_test

def test_6(data):
    """
    Test evaluation for [-5,-1,-1,-1,5,5,5,8,8,9,10,11,11]
    """
    linkedlist = LinkedList()
    for item in data[5]:
      linkedlist.append(item)

    linkedlist_test = LinkedList()
    for item in [-5,-1,5,8,9,10,11]:
      linkedlist_test.append(item)

    assert removeDuplicatesFromLinkedList(linkedlist) == linkedlist_test

def test_7(data):
    """
    Test evaluation for [1,2,3,4,5,6,7,8,9,10,11,12,12]
    """
    linkedlist = LinkedList()
    for item in data[6]:
      linkedlist.append(item)

    linkedlist_test = LinkedList()
    for item in [1,2,3,4,5,6,7,8,9,10,11,12]:
      linkedlist_test.append(item)

    assert removeDuplicatesFromLinkedList(linkedlist) == linkedlist_test
