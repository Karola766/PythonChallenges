
class NumberChecker:
    """Class that constructs numbers fitting the task requirements and checks whether
    they fit given limits"""

    def __init__(self, down, up):
        """Inclusion of set helps to avoid counting duplicate numbers"""
        self.my_set = set()
        self.down = down
        self.up = up
        self.up_length = len(str(up))
        self.down_length = len(str(down))

    def build_number(self, index, length, number):
        if index < 0 or index > length:
            return 0
        if index > 1:
            right = (number % (10 ** index)) // 10 ** (index - 1)
            if index < length:
                # Insert at the middle
                left = (number % (10 ** (index + 1))) // 10 ** index
                for i in range(left, right):
                    new = (number // (10 ** index)) * 10 ** (index + 1) + i * (
                            10 ** index) + (number % (10 ** index))
                    if self.up_length >= length + 1 >= self.down_length:
                        if self.up >= new >= self.down:
                            self.my_set.add(new)
                        return 0
                    self.build_number((length + 1) // 2, length + 1, new)
                    self.build_number(1, length + 1, new)
            else:
                # Insert at the beginning of number
                for i in range(1, right):
                    new = number + i * (10 ** index + 1)
                    if self.up_length >= length + 1 >= self.down_length:
                        if self.up >= new >= self.down:
                            self.my_set.add(new)
                        return
                    self.build_number(length + 1, length + 1, new)
                    self.build_number((length + 1) // 2, length + 1, new)
                    self.build_number(1, length + 1, new)
        else:
            # Insert after the last digit
            left = (number % (10 ** index)) // 10 ** (index - 1)
            for i in range(left, 10):
                new = number * 10 + i
                if self.up_length >= length + 1 >= self.down_length:
                    if self.up >= new >= self.down:
                        self.my_set.add(new)
                    return
                self.build_number(1, length + 1, new)
        return

    def count_passwords(self):
        if self.down > self.up:
            return 0
        for counter1 in range(1, 10):
            for counter2 in range(counter1 + 1, 10):
                number = counter1 * 1100 + counter2 * 11
                if number <= self.up:
                    if number >= self.down:
                        self.my_set.add(number)
                    # Resulting numbers should contain two pairs of different digits
                    # Additional numbers can only be inserted between, after or before
                    # the digits
                    self.build_number(4, 4, number)
                    self.build_number(2, 4, number)
                    self.build_number(1, 4, number)
                else:
                    break
        return len(self.my_set)


c = NumberChecker(372 ** 2, 809 ** 2)
print(c.count_passwords())
