class queue:
    def __init__(self):
        self.queue = []
        while True:
            choice = input("Enter your choice: 1. Enqueue 2. Dequeue 3. Peek 4. Exit: ")
            match choice:
                case "1":
                    r = input("Enter the element to enqueue: ")
                    self.queue.append(r)
                    print(f"Element enqueued: {r}")
                case "2":
                    if len(self.queue) == 0:
                        print("Queue is empty, cannot dequeue.")
                    else:
                        print(f"Item dequeued: {self.queue.pop(0)}")
                case "3":
                    if len(self.queue) == 0:
                        print("Queue is empty")
                    else:
                        print(f"Front element: {self.queue[0]}")
                case "4":
                    print("EXIT IS BEING HAPPENED")
                    break
                case _:
                    print("Invalid choice")
                    
q=queue()

# priority queue
class PriorityQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item, priority):
        # Insert item with priority
        self.queue.append((priority, item))
        # Sort the queue based on priority
        self.queue.sort()

    def dequeue(self):
        # Remove and return the item with the highest priority (lowest priority number)
        if self.queue:
            return self.queue.pop(0)[1]  # Return the item, not the priority
        else:
            return "Queue is empty."

    def peek(self):
        # Return the item with the highest priority without removing it
        if self.queue:
            return self.queue[0][1]
        else:
            return "Queue is empty."

# Example usage
pq = PriorityQueue()
pq.enqueue("Task A", 3)
pq.enqueue("Task B", 1)
pq.enqueue("Task C", 2)

print("Peek:", pq.peek())    # Task B
print("Dequeue:", pq.dequeue())  # Task B
print("Dequeue:", pq.dequeue())  # Task C
print("Dequeue:", pq.dequeue())  # Task A


class PriorityQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item, priority):
        self.queue.append((item, priority))  # Append item first, then priority
        self.queue.sort(key=lambda x: x[1])  # Sort by priority (second element)

    def dequeue(self):
        if self.queue:
            return self.queue.pop(0)[0]  # Return the item (first element of the tuple)
        else:
            return "Queue is empty."

    def peek(self):
        if self.queue:
            return self.queue[0][0]  # Return the item (first element of the tuple)
        else:
            return "Queue is empty."

# Example usage
pq = PriorityQueue()
pq.enqueue("Task A", 3)
pq.enqueue("Task B", 1)
pq.enqueue("Task C", 2)

print("Peek:", pq.peek())  # Task B
print("Dequeue:", pq.dequeue())  # Task B
print("Dequeue:", pq.dequeue())  # Task C
print("Dequeue:", pq.dequeue())  # Task A


l=[2,3,4,5,6,7,8,9]
for i in l[::-1]:
    print(i)