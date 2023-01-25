import random
import time
import copy

LIST_SIZE = 950

LIST_SIZE2 = 10000

def partition(A, p, r):
    pivot = A[r]
    smaller = p
    
    for l in range(p, r - 1):
        if A[l] <= pivot:
            (A[smaller], A[l]) = (A[l], A[smaller])
            smaller = smaller + 1
    (A[smaller], A[r]) == (A[r], A[smaller])
    return smaller

def quicksort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q -1)
        quicksort(A, q + 1, r)

def bubble_sort(a):
    finished = False
    while not finished:
        finished = True
        for i in range(0, len(a)-1):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
                finished = False

def heapify(A, size, step):
	largest = step
	left = 2 * step + 1
	right = 2* step + 2

	if left < size and A[step] < A[left]:
		largest = left

	if right < size and A[largest] < A[right]:
		largest = right

	if largest != step:
		(A[step], A[largest]) = (A[largest], A[step])

		heapify(A, size, largest)

def heapsort(A):
	size = len(A)

	for step in range(size // 2 - 1, -1, -1):
		heapify(A, size, step)

	for step in range(size - 1, 0, -1):
		(A[step], A[0]) = (A[0], A[step])
		heapify(A, step, 0)

random_numbers = []
for i in range(LIST_SIZE):
    random_numbers.append(random.randint(1, 1000))

random_numbers2 = []
for i in range(LIST_SIZE2):
    random_numbers2.append(random.randint(1, 1000))

random_numbers1 = copy.deepcopy(random_numbers)
random_numbers3 = copy.deepcopy(random_numbers2)

start_time = time.time()
quicksort(random_numbers1, 0, LIST_SIZE - 1)
end_time = time.time()
print(f"quick sort random time: {end_time - start_time}")

start_time = time.time()
quicksort(random_numbers1, 0, LIST_SIZE - 1)
end_time = time.time()
print(f"quick sort sorted time: {end_time - start_time}")

random_numbers1.reverse()
start_time = time.time()
quicksort(random_numbers1, 0, LIST_SIZE - 1)
end_time = time.time()
print(f"quick sort sorted descending time: {end_time - start_time}")

start_time = time.time()
bubble_sort(random_numbers2)
end_time = time.time()
print(f"bubble sort random time: {end_time - start_time}")

start_time = time.time()
bubble_sort(random_numbers2)
end_time = time.time()
print(f"bubble sort sorted time: {end_time - start_time}")

random_numbers2.reverse()
start_time = time.time()
bubble_sort(random_numbers2)
end_time = time.time()
print(f"bubble sort sorted descending time: {end_time - start_time}")

start_time = time.time()
heapsort(random_numbers3)
end_time = time.time()
print(f"heap sort random time: {end_time - start_time}")

start_time = time.time()
heapsort(random_numbers3)
end_time = time.time()
print(f"heap sort sorted time: {end_time - start_time}")

random_numbers3.reverse()
start_time = time.time()
heapsort(random_numbers3)
end_time = time.time()
print(f"heap sort sorted descending time: {end_time - start_time}")
