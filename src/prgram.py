import time
import random
import matplotlib.pyplot as plt

# Linear Search Function
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Function to measure search time for different list sizes
def measure_time(num_elements, target):
    arr = random.sample(range(num_elements * 2), num_elements)  # create a list of unique elements
    start_time = time.time()
    linear_search(arr, target)
    end_time = time.time()
    return end_time - start_time

# Experiment parameters
n_values = [1000, 5000, 10000, 20000, 50000, 100000, 200000]  # Different sizes of list
times = []

# Run experiment for each value of n
for n in n_values:
    target = random.randint(0, n * 2)
    time_taken = measure_time(n, target)
    times.append(time_taken)
    print(f"n = {n}, time taken = {time_taken:.6f} seconds")

# Plotting the results
plt.plot(n_values, times, marker='o')
plt.title('Linear Search Time Complexity')
plt.xlabel('Number of elements (n)')
plt.ylabel('Time taken (seconds)')
plt.grid(True)
plt.show()
