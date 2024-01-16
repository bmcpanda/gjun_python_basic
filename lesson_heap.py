import heapq
import random


class MaxHeap:
    def __init__(self):
        self.maxheap = list()

    def insert(self, data):
        heapq.heappush(self.maxheap, data)
        heapq._heapify_max(self.maxheap)

    def pop_max(self):
        max_one = heapq.heappop(self.maxheap)
        heapq._heapify_max(self.maxheap)
        return max_one

    def peek_max(self):
        return self.maxheap[0] if self.maxheap else None


class MinHeap:
    def __init__(self):
        self.minheap = list()
        heapq.heapify(self.minheap)

    def insert(self, data):
        heapq.heappush(self.minheap, data)
        # heapq._heapify_max(self.minheap)

    def pop_max(self):
        min_one = heapq.heappop(self.minheap)
        # heapq._heapify_max(self.minheap)
        return min_one

    def peek_max(self):
        return self.minheap[0] if self.minheap else None


if __name__ == '__main__':
    insert_order = random.sample(range(1, 20), 7)
    print("insert order:", insert_order)

    max_heap = MaxHeap()
    for item in insert_order:
        max_heap.insert(item)

    while max_heap.peek_max():
        print(max_heap.pop_max())
