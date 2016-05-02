"""
Description:Test for modCustomSet.py
__author__="Karma Gurung"
__date__="4/28/16"
"""

from modCustomSet import *

set1 = CustomSet([3,3,4,2,5,5,1])
set2 = CustomSet([7,8,9,2,3,2,1])
set3 = CustomSet([1,2,3,4,5,5,1,4])

print("Custome Set: " , set3)
print("\n")


union = set1.__add__(set2)

print("Union Set: ",union)
print("\n")

intersection = set2.__and__(set1)

print("Intersection Set: ",intersection)

apple1 = CustomSet([1,3,5,1])
apple2 = CustomSet([1,2,3,4])
apple3 = apple1 - apple2
apple4 = apple2 - apple1
print("---Tester for difference---")
print("set1 is a CustomSet with {1,3,5,1}:", apple1)
print("set2 is a CustomSet with {1,2,3,4}:", apple2)
print("set1 - set2 = set3 a CustomSet with {5}:", apple3)
print("set2 - set1 = set4 a CustomSet with {2,4}:", apple4)

print("\n***Test Membership***")
print("set1 is a CustomSet with {1,3,5,1}:", apple1)
print("5 in set1 is True:", 5 in apple1)

apple1 = CustomSet([1,3,1])
apple2 = CustomSet([1,2,3,4,4])
print("---Tester for subset---")
print("set1 is a CustomSet with {1,3,1}:", apple1)
print("set2 is a CustomSet with {1,2,3,4,4}:", apple2)
print("set1 <= set2 is True:", apple1 <= apple2)
print("set2 <= set1 is False:", apple2 <= apple1)

print("---Tester for Superset---")
print("set1 is a CustomSet with {1,3,1}:", apple1)
print("set2 is a CustomSet with {1,2,3,4,4}:", apple2)
print("set1 >= set2 is False:", apple1 >= apple2)
print("set2 >= set1 is True:", apple2 >= apple1)

apple1 = CustomSet([1,3,1,3])
print("---Tester for Len---")
print("set 1 is a CustomSet with {1,3,1,3}:", apple1)
print("len(set1) is 2:", len(apple1))



