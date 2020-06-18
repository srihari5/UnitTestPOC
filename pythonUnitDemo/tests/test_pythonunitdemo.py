__author__ = "Srihari"
__copyright__ = "Srihari"
__license__ = "mit"

from pythonunitdemo.pythonunitdemo import add

"""
Simple Test case example 
"""
def test_pythonunitdemo_add():
    assert add(10,30) == 40

"""
 To breakout and show AAA in simple term 
"""

def test_pythonunitdemo_add_aaa():
    # Arrange 
    value1=10
    value2=20
    # Act
    value3=value1 + value2
    #Assert
    assert value3 == 30