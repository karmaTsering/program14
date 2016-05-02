"""
Description:Test for modCustomSet.py
__author__="Karma Gurung"
__date__="4/28/16"
"""
from modCustomSet import*
print("Tester for Set")
Set1=CustomSet(1,2,3,4,5,5,5,5,1)
Set2=CustomSet()
print(Set1)
print()
print(Set2)
print("-"*80)
print("Tester for Unio Set")
print("It should print: [1,2,3,4,5]")
set3=CustomSet([1,3,5,1])
set4=CustomSet([1,2,3,4])
set5=set3+set4
print(set5)



