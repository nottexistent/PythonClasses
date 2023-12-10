'''
Name: Jordyn Kuhn
Date: 2/25/23
CRN: 23199
CIS 226: Advanced Python Programming
'''
import pytest
from vegetables import Vegetables

#test the delete function and makes sure it works
def test_add_and_del():
    v = Vegetables()
    v.add_vegetable('Carrot', '42')
    assert v.del_vegetable('Carrot') == "Carrot was successfully removed."
