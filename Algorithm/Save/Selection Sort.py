import random

class SelectionSort:
    def sort(self, nums):
        for i in range(len(nums)):
            min = i
            for j in range(i + 1, len(nums)):
                if nums[j] < nums[min]:
                    min = j
            nums[i], nums[min] = nums[min], nums[i]


selection = SelectionSort()

a = [1,564,7,9,79,7,4567,2,31,7,977,98,]
selection.sort(a)
print(a)

b = []
for x in range(10000):
    b.append(random.randint(1, 10000))
selection.sort(b)
print(b)