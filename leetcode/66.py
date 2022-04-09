class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        output = []
        str_digit = ''
        for digit in digits:
            str_digit += str(digit)
        incre_digits = int(str_digit) + 1
        
        for digit in str(incre_digits):
            output.append(int(digit))
        return output
        