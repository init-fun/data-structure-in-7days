from heapq import heappop, heapify, heappush

heap = []
heapify(heap)

heappush(heap, -1 * 10)
heappush(heap, -1 * 20)
heappush(heap, -1 * 30)
heappush(heap, -1 * 400)

print("Root node of the heap", str(-1 * heap[0]))

print("The heap elements : ")
for i in heap:
    print(f"{-1 * i}", end=" > ")
print()

element = heappop(heap)  # removing the minimum node from the hea

print("After removing min heap element")
for i in heap:
    print(f"{1 * i}", end=" > ")
print()
