class Queue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = 0
        self.rear = -1
        self.count = 0

    def is_empty(self):
        return self.count == 0

    def is_full(self):
        return self.count == self.size

    def enqueue(self):
        if self.is_full():
            print("Queue is full! Cannot enqueue.")
        else:
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = int(input("Enter the element to enqueue: "))
            self.count += 1
            print(f"Element {self.queue[self.rear]} enqueued.")

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty! Cannot dequeue.")
        else:
            print(f"Element {self.queue[self.front]} dequeued.")
            self.front = (self.front + 1) % self.size
            self.count -= 1

    def display(self):
        if self.is_empty():
            print("EMPTY HA GANDU")
        else:
            print("Current Queue:", end=" ")
            for i in range(self.count):
                position = (self.front + i) % self.size
                print(self.queue[position], end=" ")
            print()

# Example Usage
q = Queue(5)
q.enqueue()
q.enqueue()
q.enqueue()
q.enqueue()
q.enqueue()
q.display()
q.dequeue()
q.display()
