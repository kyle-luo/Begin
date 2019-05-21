def binary_search(key, low, high, count):
    if high < low:
        return -1
    mid = low + int((high - low)/2)
    if key == mid:
        return mid
    elif key > mid:
        return binary_search(key, mid + 1, high, count + 1)
    else:
        return binary_search(key, low, mid - 1, count + 1)

print(binary_search(2000, 1, 1024, 0))