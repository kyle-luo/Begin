def binary_search(key, low, high, count):
    if high < low:
        return low - 1
    mid = low + int((high - low)/2)
    print("mid:  " + str(mid))
    print("high: " + str(high))
    print("low:  " + str(low))
    if key == mid:
        return count
    elif key > mid:
        return binary_search(key, mid + 1, high, count + 1)
    else:
        return binary_search(key, low, mid - 1, count + 1)

print(binary_search(239, 1, 1024, 0))