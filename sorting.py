# Bubble Sort
def bubblesort(a):
    print("\n--- Bubble Sort ---")
    steps = 0
    n = len(a)
    for i in range(n - 1):
        print(f"\nPass {i + 1}:")
        for j in range(n - 1 - i):
            if a[j] > a[j + 1]:
                print(f"  Swapping {a[j]} and {a[j + 1]}")
                a[j], a[j + 1] = a[j + 1], a[j]
            else:
                print(f"  No swap needed for {a[j]} and {a[j + 1]}")
        steps += 1
        print("  After Pass", steps, ":", a)
    print("Sorted array:", a)
    print("Total Steps:", steps)

# Selection Sort
def selectionsort(a):
    print("\n--- Selection Sort ---")
    steps = 0
    for i in range(len(a)):
        min_index = i
        for j in range(i + 1, len(a)):
            if a[j] < a[min_index]:
                min_index = j
        a[i], a[min_index] = a[min_index], a[i]
        steps += 1
        print("Step", steps, ":", a)
    print("Sorted array:", a)
    print("Total Steps:", steps)

# Insertion Sort
def insertionsort(a):
    print("\n--- Insertion Sort ---")
    steps = 0
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
        steps += 1
        print("Step", steps, ":", a)
    print("Sorted array:", a)
    print("Total Steps:", steps)

# Main Code
data = [5, 2, 9, 1, 5, 6]

print("Original Array:", data)

# Use .copy() to keep original array unchanged for each sort
bubblesort(data.copy())
selectionsort(data.copy())
insertionsort(data.copy())
