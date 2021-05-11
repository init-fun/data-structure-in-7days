from heapq import heappush, heappop, heapify


def kth(arr, k):
    heap = []
    heapify(heap)
    for i in arr:
        heappush(heap, i)
        while len(heap) > k:
            heappop(heap)

    return heap


lst = [7, 10, 4, 3, 20, 15]
k = 3
print(kth(lst, k))