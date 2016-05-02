"""
Description: This is the modCustomSet
__author__="Karma,Anisha, Priyash"
__date__="4/22/16"
"""
#WWW

#Priyash Kafle
def __and__(self,other):
    '''
    Description: Returns an intersection of two sets 
    PreCOndition: other(list)
    PostCondition: None
    '''
    newSet=[]
    for i in self._setList:
        if i in other._setList:
            newSet.append(i)
    otherSet=CustomSet(newSet)

    return newSet

def __sub__(self, other):
    '''
    Description: Returns the unique element of set 1
    PreCondition: other(list)
    PostCondition: None
    '''
    myList=[]
    for item in self._setList:
        if item not in other._setList:
            myList=myList.append(item)

def __contains__(self,other):
    '''
    Description: Checks if an element is in the set
    PreCOndition: other(integer)
    POstCondition: None
    '''
    if other in self._setList:
        return "yes"
    else:
        return "not there"
