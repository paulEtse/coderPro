def single_number(nums):
    found = set()
    for n in nums:
        if n in found:
            found.remove(n)
        else:
            found.add(n)
    return found.pop()


def single_number__o_n_space(nums):
    for i in range(len(nums)):
        if nums[i] not in nums[: i] + nums[i + 1:]:
            return nums[i]
    raise Exception("Not found")
