from utils.stack import Stack


class Solution:
    def isValid(self, s):
        stack = Stack()
        open_bracket_dict = {"(": ")", "{": "}", "[": "]"}
        close_bracket_dict = {")": "(", "}": "{", "]": "["}
        for character in s:
            if character in open_bracket_dict:
                stack.push(character)
            elif character in close_bracket_dict:
                if stack.top() == close_bracket_dict[character]:
                    stack.pop()
                else:
                    return False
            else:
                raise ("Invalid string")
        return stack.empty()
