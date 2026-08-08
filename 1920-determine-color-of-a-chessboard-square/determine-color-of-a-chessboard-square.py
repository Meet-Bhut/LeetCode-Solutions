class Solution(object):
    def squareIsWhite(self, coordinates):
        black=["a","c","e","g"]
        if coordinates[0] in black:
            if int(coordinates[1])%2!=0:
                return False
            else:
                return True
        else:
            if int(coordinates[1])%2==0:
                return False
            else:
                return True
