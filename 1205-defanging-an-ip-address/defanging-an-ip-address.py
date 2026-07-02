class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        ans=address.split(".")
        return "[.]".join(ans)


        