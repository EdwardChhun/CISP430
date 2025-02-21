class Node: #a node of a linked list

    def __init__(self, node_data): #create new node
        self._data = node_data
        self._next = None

    def get_data(self): #getter for data
        return self._data

    def set_data(self, node_data): #setter for data
        self._data = node_data

    data = property(get_data, set_data) #encapsulation for data
    
    def get_next(self): #getter for next
        return self._next

    def set_next(self, node_next): #setter for next
        self._next = node_next

    next = property(get_next, set_next) #encapsulation for next
    
    def __str__(self): #overloads string operator
        return str(self._data)


class LinkedList():
    """Linked List class implementation"""

    def __init__(self): #Create a linked list
        self._head = None
        self._count = 0

    def is_empty(self): #Is the list empty?
        return self._head is None

    def size(self): #Size of the list
        return self._count

    def __len__(self): #Size of the list
        return self._count

    def __str__(self): #List as a stringE
        list_str = "["
        current = self._head

        while current:
            list_str += str(current)
            if current.next:
                list_str += ", "
            current = current.next
        list_str += "]"
        return list_str

    def add(self, value): #Add a new node
        new_node = Node(value)
        new_node.set_next(self._head)
        self._head = new_node
        self._count += 1 

    def append(self, value):
        new_node = Node(value)
        if not self._head:
            self._head = new_node
        else:
            current = self._head
            while current.next:
                current = current.next
            current.next = new_node
        self._count += 1
            
        
    def remove(self, value): #Remove a node with a specific value
        curr = self._head
        prev = None
        while curr:
            if curr.data == value:
                if prev is None:
                    self._head = curr.next
                else:
                    prev.next = curr.next
                self._count -= 1
                return
            prev = curr
            curr == curr.next
        raise ValueError(f"{value} is not in the list")

    def search(self, value): #Search for a node with a specific value
        curr = self._head
        while curr:
            if curr.data == value:
                return True
            curr = curr.next
        return False

class CircularList(LinkedList):
    def __init__(self): #Create an Circular linked list"""
        LinkedList.__init__(self)
        self._tail=None

    def add(self, value): #Add a new node
        new_node = Node(value)

        if self._head is None:
            self._head = new_node
            self._tail = new_node
            self._tail.set_next(self._head) 
        else:
            new_node.set_next(self._head)
            self._head = new_node
            self._tail.set_next(self._head)
            
        self._count += 1 
        
    def append(self, value):
        new_node = Node(value)

        if self._head is None:  
            self._head = new_node
            self._tail = new_node
            self._tail.set_next(self._head)  
        else:  
            self._tail.set_next(new_node)  
            self._tail = new_node  
            self._tail.set_next(self._head) 

        self._count += 1
    def white_elephant(self, old_value, new_value): # Function for white elephant simulation
        pass
    
    def __str__(self): #overload string operator
        cur=self._head
        list_str="["
        #you'll probably want to change the kind of loop
        for _ in range(self._count):
            list_str += str(cur)
            if cur.next != self._head:
                list_str += ", "
            cur = cur.next
        list_str += "]"
        return list_str


if __name__=="__main__":
    
    # white elephant function
    def foo(mylist) -> None:
        """ 
        mylist: Circularlist()
        info: the nodes of the list are tuples (position, # of presents)
        e.g: (1, 2) => first position with two presents
        """
        curr = mylist._head 
        
        while True:
        
            # If the current person has a atleast a present
            if curr._data[1]:
                
                # Finding the next person who has a gift to steal from
                while not curr.next._data[1]:
                    curr.next = curr.next.next
                
                # Steal the next person's gift
                curr.set_data((curr._data[0], curr._data[1] + curr.next._data[1]))
                
                # The next person would have 0 gifts
                curr.next.set_data((curr.next._data[0], 0))
                
                # Printing the current person having n-amount of gifts "(position number, # gifts)""
                # NOTE: Remove the 2 print statements below to see how the values of the linked list behave
                # print(f"stole present: {curr._data}")
                # print(mylist)
                
            # If the current person has everyone's presents , exit the loop
            if curr._data[1] == len(mylist):
                print(f"\nFriend {curr._data[0]} with {curr._data[1]} presents")
                break
            
            curr = curr.next

    testCase = CircularList()
    myList = CircularList()
    
    # 5 People
    for i in range(1, 5 + 1):
        testCase.append((i, 1)) # [position, amount of presents]
    
    # 3018458 People
    for i in range(1, 3018458 + 1):
        myList.append((i, 1))
        
    foo(testCase)
    foo(myList)
    

    

