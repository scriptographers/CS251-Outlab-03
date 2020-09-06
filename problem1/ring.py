class RingInt(object):
    """Class for Modular Arithmetic"""

    def __init__(self, value, characteristic):
        super(RingInt, self).__init__()
        self.characteristic = characteristic
        self.value = value % characteristic

    def __str__(self):
        return "{}[{}]".format(self.value, self.characteristic)

    def __add__(self, other):
        if self.characteristic != other.characteristic:
            raise ValueError("Characteristics don't match")
        else:
            new_value = (self.value + other.value) % self.characteristic
            return RingInt(new_value, self.characteristic)

    def __sub__(self, other):
        if self.characteristic != other.characteristic:
            raise ValueError("Characteristics don't match")
        else:
            new_value = (self.value - other.value) % self.characteristic
            return RingInt(new_value, self.characteristic)

    def __mul__(self, other):
        if self.characteristic != other.characteristic:
            raise ValueError("Characteristics don't match")
        else:
            new_value = (self.value * other.value) % self.characteristic
            return RingInt(new_value, self.characteristic)

    def __truediv__(self, other):
        if self.characteristic != other.characteristic:
            raise ValueError("Characteristics don't match")
        oth_inv = other.inverse()
        if oth_inv:
            new_value = (self.value * oth_inv) % self.characteristic
            return RingInt(new_value, self.characteristic)
        else:
            raise ValueError("Division of {} undefined".format(other))

    def __pow__(self, power):
        if power < 0:
            inv = self.inverse()
            if inv:
                return RingInt(inv, self.characteristic) ** (-1 * power)
            else:
                raise ValueError("Negative Powers of {} undefined".format(self))
        if power == 0:
            return RingInt(1, self.characteristic)
        if self.value == 0:
            return RingInt(0, self.characteristic)
        x = self.value
        y = 1
        while power:
            if power % 2 == 1:
                y = (y * x) % self.characteristic
            power = power // 2
            x = (x * x) % self.characteristic
        return RingInt(y, self.characteristic)

    def __eq__(self, other):
        if self.characteristic != other.characteristic:
            raise ValueError("Characteristics don't match")
        else:
            if self.value == other.value:
                return True
            else:
                return False

    def inverse(self):
        if self.value == 0:
            return None
        elif self.value == 1:
            return 1

        # Using Extended Euclid's Algorithm
        last_r, r = self.value, self.characteristic
        x, last_x, y, last_y = 0, 1, 1, 0

        while r:
            last_r, (quotient, r) = r, divmod(last_r, r)
            x, last_x = last_x - quotient * x, x
            y, last_y = last_y - quotient * y, y

        if last_r != 1:
            return None
        if last_x < 0:
            return last_x + self.characteristic
        return last_x


if __name__ == '__main__':
    a = RingInt(0, 7)
    b = RingInt(6, 7)
    c = a ** 0
    print(c)
