class Solution:
    def smallestNumber(self, n: int) -> int:
        if n <= 0b1:
            return 0b1
        if n <= 0b11:
            return 0b11
        if n <= 0b111:
            return 0b111
        if n <= 0b1111:
            return 0b1111
        if n <= 0b11111:
            return 0b11111
        if n <= 0b111111:
            return 0b111111
        if n <= 0b1111111:
            return 0b1111111
        if n <= 0b11111111:
            return 0b11111111
        if n <= 0b111111111:
            return 0b111111111
        if n <= 0b1111111111:
            return 0b1111111111
        return 0