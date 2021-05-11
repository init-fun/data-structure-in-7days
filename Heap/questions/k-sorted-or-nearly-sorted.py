from heapq import heappush, heappop, heapify


def nearly_sorted(arr, k):
    heap = []
    res = []
    heapify(heap)
    for i in arr:
        heappush(heap, i)
        while len(heap) > k:
            popped_ele = heappop(heap)
            res.append(popped_ele)
    while heap:
        res.append(heappop(heap))
    return res


arr = [6, 5, 3, 2, 8, 10, 9]
print(nearly_sorted(arr, 3))