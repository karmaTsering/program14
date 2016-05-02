"""
Description: THis program create set intersection, union, 
"""
class CustomSet:
    
    def __init__(self, tmp1):
        """
        __author__="Karma Gurung"
        __date__="4/27/16"
        Description: This
        Pre-condition:
        Post-condition:
        
        """
        self._setList=[]
        for el in tmp1:
            if el not in self._setList:
               self._setList.append(el)


    def __add__(self, set,tmp2):
        """
        __author__="Karma Gurung"
        __date__="4/27/16"
        Description:
        Pre-condition:
        Post-condition:
        """
        newSet=[]
        Set=[]
        for i in self._setList:
            newSet.append(i)
        for i in other._SetList:
            newSet.append(i)

        for el in newSet:
            if el not in Set:
                Set.append(el)
        return Set
        
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

    def subset(self,tmp1,tmp2):
        set1 = CustomSet.__init__(self,tmp1)
        set2 = CustomSet.__init__(self, tmp2)
        ct = 0
        for el in tmp1:
            if el in tmp2:
                ct +=1
        if ct == len(tmp1):
            return ("Yes")
        if ct < len(tmp1):
            return ("not a subset")

    
    def superSet(self,tmp1,tmp2):
        set1 = CustomSet.__init__(self,tmp1)
        set2 = CustomSet.__init__(self, tmp2)
        ct = 0
        for el in tmp1:
            if el in tmp2:
                ct +=1
        if ct == len(tmp1) and len(tmp1) < len(tmp2):
            return ("Yes")
        else:
            return ("No")

    def count(self, tmp1):
        set1 = CustomSet.__init__(self,tmp1)
        ct = 0
        for el in tmp1:
            ct += 1
        return ct
    
    def __str__(self):
        """
        __author__="Karma Gurung"
        __date__="4/27/16"
        Description:
        Pre-condition:
        Post-condition:
        """
        
        tmp=','.join(str(el) for el in self._setList)
        outPut="{"+tmp+"}"
        return outPut
