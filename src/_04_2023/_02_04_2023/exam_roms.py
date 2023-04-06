import heapq


class ExamRoom(object):
    """
    https://leetcode.com/problems/exam-room/description/
    """

    def __init__(self, n):
        """
        :type n: int
        """
        self.n = n
        self.heap = []
        self.available_start = {}
        self.available_last = {}

        self.push_segment(0, self.n - 1)

    def push_segment(self, start, end):
        if start == 0 or end == self.n - 1:
            priority = end - start
        else:
            priority = (end - start) // 2

        segment = [-priority, start, end, True]
        heapq.heappush(self.heap, segment)

        self.available_start[start] = segment
        self.available_last[end] = segment

    def seat(self):
        """
        :rtype: int
        """
        while True:
            _, first, last, is_valid = heapq.heappop(self.heap)
            if is_valid:
                del self.available_start[first]
                del self.available_last[last]
                break

        if first == 0:
            next_seat = 0
            if first != last:
                self.push_segment(first + 1, last)
        elif last == self.n - 1:
            next_seat = self.n - 1
            self.push_segment(first, last - 1)
        else:
            next_seat = first + (last - first) // 2

            if next_seat > first:
                self.push_segment(first, next_seat - 1)
            if next_seat < last:
                self.push_segment(next_seat + 1, last)

        return next_seat

    def leave(self, p):
        """
        :type p: int
        :rtype: None
        """
        left = p - 1
        right = p + 1

        first = p
        last = p

        if left > 0 and left in self.available_last:
            segment_left = self.available_last.pop(left)
            segment_left[3] = False
            first = segment_left[1]

        if right < self.n and right in self.available_start:
            segment_right = self.available_start.pop(right)
            segment_right[3] = False
            last = segment_right[2]

        self.push_segment(first, last)
