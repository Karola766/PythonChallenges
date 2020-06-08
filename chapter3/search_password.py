import math


# ok, whatever, because the constraints make the whole thing have to be 6 digits long.
# which gives us 2 recurring digits and 2 recursions adding to that

class checker:

    def __init__(self):
        self.my_set = set()

    def build_number(self, index, length, number, down, up):
        if index < 0 or index > length:
            return 0
        if index > 1:
            right = (number % (10 ** index)) // 10 ** (index - 1)
            if index < length:
                # middle insert
                left = (number % (10 ** (index + 1))) // 10 ** (index)
                for i in range(left, right):
                    new = (number // (10 ** index)) * 10 ** (index + 1) + i * (
                            10 ** index) + (number % (10 ** index))
                    if length + 1 == 6:
                        if up >= new >= down:
                            self.my_set.add(new)
                        return 0
                    self.build_number((length + 1) // 2, length + 1, new, down, up)
                    self.build_number(1, length + 1, new, down, up)
            else:
                # index of length
                # inserting at the beginning
                for i in range(1, right):
                    new = number + i * (10 ** index + 1)
                    if length + 1 == 6:
                        if up >= new >= down:
                            self.my_set.add(new)
                        return
                    self.build_number(length + 1, length + 1, new, down, up)
                    self.build_number((length + 1) // 2, length + 1, new, down, up)
                    self.build_number(1, length + 1, new, down, up)
        else:
            # right at the end
            left = (number % (10 ** index)) // 10 ** (index - 1)
            for i in range(left, 10):
                new = number * 10 + i
                if length + 1 == 6:
                    if up >= new >= down:
                        self.my_set.add(new)
                    return
                self.build_number(1, length + 1, new, down, up)
        return

    def count_passwords(self, down, up):
        if down > up:
            return 0
        length = 4
        for counter1 in range(1, 10):
            for counter2 in range(counter1 + 1, 10):
                number = counter1 * 1100 + counter2 * 11
                if number <= up:
                    if number >= down:
                        self.my_set.add(number)
                    self.build_number(4, length, number, down, up)
                    self.build_number(2, length, number, down, up)
                    self.build_number(1, length, number, down, up)
                else:
                    break
        return len(self.my_set)


c = checker()
print(c.count_passwords(372 ** 2, 809 ** 2))
print(c.my_set)
