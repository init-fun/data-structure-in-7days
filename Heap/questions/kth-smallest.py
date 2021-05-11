from heapq import heappop, heappush, heapify


def kth(arr, k):
    max_heap = []
    heapify(max_heap)
    for i in arr:
        heappush(max_heap, -1 * i)
        if len(max_heap) > k:
            heappop(max_heap)

    return -1 * heappop(max_heap)


lst = [7, 10, 4, 3, 20, 15]
k = 3
print(kth(lst, k))
