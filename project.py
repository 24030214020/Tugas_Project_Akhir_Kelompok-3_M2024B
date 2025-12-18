import pandas as pd
import math
import time

df = pd.read_csv("tmdb_5000_movies.csv")

judul = df["title"].fillna("").tolist()
tahun = df["release_date"].fillna("").tolist()

film_data = list(zip(judul, tahun))
judul_list = [x[0] for x in film_data]

target = input("Masukkan judul film yang ingin dicari: ")

def linear_search(arr, target):
    for i, x in enumerate(arr):
        if x == target:
            return i
    return -1

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def jump_search(arr, target):
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0

    while prev < n and arr[min(step, n)-1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1

    for i in range(prev, min(step, n)):
        if arr[i] == target:
            return i
    return -1

sizes = [2000, 3000, 5000]

for size in sizes:
    subset = film_data[:size]
    subset_titles = [x[0] for x in subset]
    sorted_subset = sorted(subset_titles)

    start = time.perf_counter()
    i_linear = linear_search(subset_titles, target)
    t_linear = math.ceil((time.perf_counter() - start)*1_000_000)

    start = time.perf_counter()
    i_binary = binary_search(sorted_subset, target)
    t_binary = math.ceil((time.perf_counter() - start)*1_000_000)

    start = time.perf_counter()
    i_jump = jump_search(sorted_subset, target)
    t_jump = math.ceil((time.perf_counter() - start)*1_000_000)

    print("====================================")
    print("Dataset ukuran :", size)

    if i_linear != -1:
        idx = i_linear
        print("film ditemukan :", subset[idx][0], "| tahun :", subset[idx][1])
    else:
        print("film tidak ditemukan pada dataset ukuran ini")

    print("waktu linear search :", t_linear , "μs")
    print("waktu binary search :", t_binary, "μs")
    print("waktu jump search   :", t_jump, "μs")
    print()