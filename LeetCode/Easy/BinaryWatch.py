"""
 A binary watch has 4 LEDs on the top to represent the hours (0-11), and 6 LEDs on the bottom to represent the minutes (0-59). Each LED represents a zero or one, with the least significant bit on the right.

    For example, the below binary watch reads "4:51".

Given an integer turnedOn which represents the number of LEDs that are currently on (ignoring the PM), return all possible times the watch could represent. You may return the answer in any order.

The hour must not contain a leading zero.

    For example, "01:00" is not valid. It should be "1:00".

The minute must consist of two digits and may contain a leading zero.

    For example, "10:2" is not valid. It should be "10:02".


Example 1:

Input: turnedOn = 1
Output: ["0:01","0:02","0:04","0:08","0:16","0:32","1:00","2:00","4:00","8:00"]

Example 2:

Input: turnedOn = 9
Output: []


Constraints:
    0 <= turnedOn <= 10

"""

class Solution(object):
    def readBinaryWatch(self, turnedOn):
        """
        :type turnedOn: int
        :rtype: List[str]
        """
        times = []
        # Loop through hours 0-11 and minutes 0-59
        for h in range(12):
            for m in range(60):
                # Use bin().count('1') for compatibility with Python < 3.10
                if (bin(h).count('1') + bin(m).count('1')) == turnedOn:
                    # Use .format() for compatibility with Python < 3.6
                    times.append("{}:{:02d}".format(h, m))
        return times

solution = Solution()
print("0 =>", solution.readBinaryWatch(0), end="\n\n")
print("1 =>", solution.readBinaryWatch(1), end="\n\n")
print("2 =>", solution.readBinaryWatch(2), end="\n\n")
print("3 =>", solution.readBinaryWatch(3), end="\n\n")
print("4 =>", solution.readBinaryWatch(4), end="\n\n")
print("5 =>", solution.readBinaryWatch(5), end="\n\n")
print("6 =>", solution.readBinaryWatch(6), end="\n\n")
print("7 =>", solution.readBinaryWatch(7), end="\n\n")
print("8 =>", solution.readBinaryWatch(8), end="\n\n")
print("9 =>", solution.readBinaryWatch(9), end="\n\n")
print("10 =>", solution.readBinaryWatch(10), end="\n\n")