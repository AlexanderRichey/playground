def merge_sort(arr, cb=lambda a, b : a < b):
    arr_len = len(arr)
    if arr_len <= 1:
        return arr

    middle = int(arr_len / 2)
    left = arr[:middle]
    right = arr[middle:]

    return _merge(merge_sort(left, cb), merge_sort(right, cb), cb)


def _merge(left, right, cb):
    merged = []

    while len(left) and len(right):
        if cb(left[0], right[0]):
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))

    return merged + left + right


def quick_sort(arr, cb=lambda a, b : a < b):
    arr_len = len(arr)
    if arr_len == 0:
        return []
    elif arr_len == 1:
        return arr

    middle = int(arr_len / 2)
    pivot = arr.pop(middle)

    left = []
    right = []
    while len(arr):
        val = arr.pop()
        if cb(val, pivot):
            left.append(val)
        else:
            right.append(val)
    return quick_sort(left, cb) + [pivot] + quick_sort(right, cb)


def heap_sort(arr, cb=lambda a, b : a < b):
    heap = _heapify(arr)




def _heapify(arr):
    class HeapNode:
        def __init__(self, val):
            self.val = val
            self.left = None
            self.right = None
    class Heap:
        def __init__(self, head):
            self.head = head
        def add(self, val):
            node = self.head
            while node:
                if node.left:
                    node = node.left
                elif node.right:
                    node = node.right
                elif node.left and not node.right:
                    node.right = HeapNode(val)
                    node = None
                elif node.right and not node.left:
                    node.left = HeapNode(val)
                    node = None
        def swap(self):
            pass
    for i in arr:
        heap.add(i)
    return heap

def _swap(arr, a, b):
    arr[b], arr[a] = arr[a], arr[b]
    return arr
