from multiprocessing import Pool
import random as rd
import time
import matplotlib.pyplot as plt


def parallel_sort(data, processes=2):
    chunk_size = len(data) // processes
    chunks = [data[i * chunk_size:(i + 1) * chunk_size] for i in range(processes)]

    with Pool(processes=processes) as pool:
        sorted_chunks = pool.map(sorted, chunks)

    result = []
    for chunk in sorted_chunks:
        result.extend(chunk)
    return sorted(result)



data_sizes = [100, 10**3, 10**4, 10**5, 10**6, 10**7]
process_counts = [1, 2, 4, 8, 16]
results = {}
for size in data_sizes:
    results[size] = []
    data = [rd.randint(1, 100) for _ in range(size)]
    for proc in process_counts:
        start_time = time.time()
        parallel_sort(data, proc)
        elapsed_time = time.time() - start_time
        results[size].append(elapsed_time)

for size in data_sizes:
    plt.plot(process_counts, results[size], label=f'Data Size = {size}')

plt.xlabel('Number of Processes')
plt.ylabel('Time (s)')
plt.legend()
plt.show()


# For whatever reason on machine the performance is roughly the same
