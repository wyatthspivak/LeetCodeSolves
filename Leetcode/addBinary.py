from typing import Optional


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = len(a) - 1
        j = len(b) - 1

        carry = 0

        output_string = ""

        while i >= 0 or j >= 0 or carry == 1:

            if i >= 0:
                carry += int(a[i])

            i -= 1

            if j >= 0:
                carry += int(b[j])

            j -= 1

            output_string += str(carry % 2)

            carry //= 2

        return output_string[::-1]




