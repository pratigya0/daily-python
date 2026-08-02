# Define a class named Queue
# A class is like a blueprint for creating queue objects.
class queue:
    def __init__(self):
        self.values = []
    def enqueue(self, x):
        self.values.append(x)
    def dequeue(self):
        front = self.values[0]

        self.values = self.values[1:]

        return front 

q1=queue()
q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)
print(q1.values)
print(q1.dequeue())
print(q1.values)


'''# Create an empty queue (using a list)
stock_price_queue = []

# Insert stock prices at the front
stock_price_queue.insert(0,131.10)
stock_price_queue.insert(0,132.12)
stock_price_queue.insert(0,135)

#Print the queue
print(stock_price_queue)

# Remove the oldest element (FIFO)
removed = stock_price_queue.pop()

print("Removed:", removed)
print("Queue after pop:", stock_price_queue)'''
