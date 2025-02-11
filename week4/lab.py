from queueADT import Queue
from random import randint

custQ = Queue()   # Line (queue) of customers containing the
      	#   time that each customer arrived and
      	#   joined the line
simLength=0   	# Length of simulation (minutes)
minute=0      	# Current minute
timeArrived=0 	# Time dequeued customer arrived
waitTime=0    	# How long dequeued customer waited
totalServed = 0   # Total customers served
totalWait   = 0   # Total waiting time
maxWait 	= 0   # Longest wait
numArrivals = 0

print("Welcome to Edward's Bank")
simLength=int(input("Enter the length of time to run the simulator : "))

for minute in range(simLength):
    if (not custQ.is_empty()):
		#1) dequeue the first customer and capture its return in timeArrived
        timeArrived=custQ.dequeue()
		#2) increment totalServed
        totalServed+=1
		#3) calculate the waitTime of the customer
        waitTime=minute-timeArrived
		#4) add the waitTime of the customer to totalWait
        totalWait+=waitTime
		#5) update maxWait if this customer waited longer than any previous customer.
        if waitTime>maxWait:
                maxWait=waitTime
                   	 
    numArrivals=randint(0,4)
	#print(numArrivals)
    for j in range(numArrivals):
            custQ.enqueue(minute)
       	 


print("Customers served : ",totalServed)
print("Average wait 	: ",totalWait/totalServed,"minutes")
print("Longest wait 	: ",maxWait,"minutes")

