class Solution:
    def getRange(self, arr, target):
        start = 0
        end = len(arr)
        found = False
        while not (found) and start <= end:
            middle = int((start + end) / 2)
            if arr[middle] == target:
                found = True
            elif arr[middle] < target:
                start = middle + 1
            else:
                end = middle - 1
        if not (found):
            return [-1, -1]
        end = start = middle
        while start > 0 and arr[start] == target:
            start -= 1
        while end < len(arr) and arr[end] == target:
            end += 1
        return [start + 1, end - 1]
