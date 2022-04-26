def pythagoreanTriplets(nums):
    nums_square = []
    for n in nums:
        nums_square.append(n ** 2)
    nums_square.sort()

    for i in range(len(nums)):
        j = 0
        k = i - 1
        while j < k:
            if nums_square[i] == nums_square[j] + nums_square[k]:
                return True
            else:
                if nums_square[i] > nums_square[j] + nums_square[k]:
                    j += 1
                else:
                    k -= 1
    return False
