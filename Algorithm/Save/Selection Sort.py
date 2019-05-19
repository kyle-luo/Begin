import random


def selection_sort(nums):
    for i in range(len(nums)):
        min = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[min]:
                min = j
        nums[i], nums[min] = nums[min], nums[i]


a = [1,564,7,9,79,7,4567,2,31,7,977,98,]
selection_sort(a)
print(a)

b = []
for x in range(10000):
    b.append(random.randint(1, 100000))
selection_sort(b)
print(b)