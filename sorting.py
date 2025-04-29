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

# Quick Sort
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    small = []
    big = []
    
    for i in arr[1:]:
        if i < pivot:
            small.append(i)
        else:
            big.append(i)
    return quicksort(small) + [pivot] + quicksort(big)

# Merge Sort
def mergesort(arr):
    print("\n--- Merge Sort ---")
    steps = [0]

    def merge_sort_inner(a):
        if len(a) <= 1:
            return a

        mid = len(a) // 2
        left = merge_sort_inner(a[:mid])
        right = merge_sort_inner(a[mid:])

        merged = []
        i = j = 0
        print(f"  Merging: {left} and {right}")
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1

        merged.extend(left[i:])
        merged.extend(right[j:])
        steps[0] += 1
        print(f"  Step {steps[0]}: {merged}")
        return merged

    sorted_arr = merge_sort_inner(arr)
    print("Sorted array:", sorted_arr)
    print("Total Steps:", steps[0])

# Main Code
data = [10, 7, 4, 9, 77, 44]
print("Original Array:", data)

bubblesort(data.copy())
selectionsort(data.copy())
insertionsort(data.copy())
mergesort(data.copy())

sorted_quick = quicksort(data.copy())
print("\n--- Quick Sort ---")
print("Sorted array:", sorted_quick)
