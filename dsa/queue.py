'''class queue:
    def __init__(self):
        self.values = []
    def enqueue(self, x):
        self.values.append(x)
    def dequeue(self):
        front = self.values[0]

        self.values = self.values[1:]

        return front '''



wmt_stock_price_queue = []

wmt_stock_price_queue.insert(0,131.10)

wmt_stock_price_queue.insert(0,132.12)

wmt_stock_price_queue.insert(0,135)

print(wmt_stock_price_queue)

removed = wmt_stock_price_queue.pop()

print("Removed:", removed)
print("Queue after pop:", wmt_stock_price_queue)
