class Queue:
	#Queue implementation as a list
    def __init__(self):
        #Create new queue
        self._items = []
    
    def is_empty(self):
        #Check if the queue is empty
        return len(self._items)==0
    
    def enqueue(self, item):
        #Add an item to the queue
        self._items.insert(0, item)
    
    def dequeue(self):
        #Remove an item from the queue
        return self._items.pop()

    
    def size(self):
        #Get the number of items in the queue
        return len(self._items)

if __name__=="__main__":
	q = Queue()
	q.enqueue(4)
	q.enqueue(5)
	q.enqueue(6)
	print("size=",q.size())
	print("is empty?",q.is_empty())
	q.enqueue(8)
	print("dequeue",q.dequeue())
	print("dequeue",q.dequeue())
	print("size=",q.size())

