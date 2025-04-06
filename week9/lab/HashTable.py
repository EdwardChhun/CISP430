
from LinkedList import LinkedList

class Password():

    def __init__(self,uname="-",pwd="-"):
        self.username=uname
        self.password=pwd

    def setKey (self, newKey):
        self.username = newKey

    def getKey (self):
        return self.username

    def __eq__(self,other):
        return self.username==other.username

	#this hash converts a string to an integer
    def hash(self):
        val = 0
        for i in range(len(self.username)):
            val += ord(self.username[i])
        return val
    
    def __str__(self,hidden=True):
        if hidden:
            return self.username
        else:
            return "u: "+self.username+"  p: "+self.password


class HashTable():
    def __init__ (self, initTableSize):
        self.tableSize=initTableSize
        self.dataTable =[None]*initTableSize

    def put (self,newDataItem):
        # apply two hash functions: 1. convert string (username) to integer
        # 2. use the division method (% tableSize) to get the index
        index = newDataItem.hash() % self.tableSize

        if (self.dataTable[index] is None):
            self.dataTable[index] = LinkedList()
        else:
            if self.dataTable[index].search(newDataItem):#if it is already there
                self.dataTable[index].remove(newDataItem)#remove it
            #then insert the data (Password stuff) into the HashTable
        self.dataTable[index].add(newDataItem)
        #print(index,newDataItem)


    def get(self, searchKey):
        # apply two hash functions: 1. convert string (searchkey) to integer
        # 2. use the division method (% tableSize) to get the index
        dataItem=Password(searchKey)
        index = dataItem.hash() % self.tableSize

        #if there is nothing at that index, then the searchkey isn't in the
        #table
        if (self.dataTable[index] is None):
            return False
        else:
            return self.dataTable[index].search(dataItem)

    def clear(self):
        for i in range(self.tableSize):
            self.dataTable[i]=None


    def is_empty(self):
        for i in range(self.tableSize):
            if (self.dataTable[i] is not None):
                return False

        return True

    def __str__(self):
        if self.is_empty():
            return "The hash table is empty"
        outStr=""
        outStr+="The Hash Table has the following entries\n"
        for i in range(self.tableSize):
            outStr+=str(i)+ ": "
            if (self.dataTable[i] is None ):
                outStr+="---"
            else:
                outStr+=str(self.dataTable[i])
            outStr+="\n"
        return outStr
