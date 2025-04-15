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
                    
q = queue()
