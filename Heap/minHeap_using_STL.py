from heapq import heappop, heappush, heapify

heap = []
heapify(heap)

heappush(heap, 10)
heappush(heap, 30)
heappush(heap, 20)
heappush(heap, 400)

print("Root node of the heap", str(heap[0]))

print("The heap elements : ")
for i in heap:
    print(f"{i}", end=" > ")
print()

element = heappop(heap)  # removing the minimum node from the hea

print("After removing min heap element")
for i in heap:
    print(f"{i}", end=" > ")
print()
