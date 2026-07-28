class Solution(object):
    def countAsterisks(self, s):
        inside = False
        count = 0

        for char in s:
            if char == '|':
                inside = not inside
            elif char == '*' and not inside:
                count += 1

        return count
        