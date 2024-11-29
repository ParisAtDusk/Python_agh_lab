import random as rd

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

N = 10
rng = []
for n in range(N):
    rng.append(rd.randint(0, 10))

bb_sort = bubble_sort(rng)
qk_sort = quick_sort(rng)
int_sort = sorted(rng)

print("Random numbers: ", rng)
print("Bubble sort: ", bb_sort)
print("Quick sort: ", qk_sort)
print("Integrated sorted: ", int_sort)

assert bb_sort == int_sort, "Bubble Sort is incorrect"
assert qk_sort == int_sort, "Quick Sort is incorrect"
print("Ok, exiting")


