class RingInt(object):
    """Class for Modular Aritmatic"""
    def __init__(self, value, characteristic):
        super(RingInt, self).__init__()
        self.characteristic = characteristic
        self.value = value

    def __str__(self):
        return "{}[{}]".format(self.value, self.characteristic)

    def __add__(self, other):
        if (self.characteristic != other.characteristic):
            raise ValueError("Characteristics don't match")
        else:
            new_value = (self.value + other.value)%self.characteristic
            return RingInt(new_value, self.characteristic)

    def __sub__(self, other):
        if (self.characteristic != other.characteristic):
            raise ValueError("Characteristics don't match")
        else:
            new_value = (self.value - other.value)%self.characteristic
            return RingInt(new_value, self.characteristic)

    def __mul__(self, other):
        if (self.characteristic != other.characteristic):
            raise ValueError("Characteristics don't match")
        else:
            new_value = (self.value*other.value)%self.characteristic
            return RingInt(new_value, self.characteristic)

    def __truediv__(self, other):
        if (self.characteristic != other.characteristic):
            raise ValueError("Characteristics don't match")
        # complete this

    def __pow__(self, power):
        # complete this

    def __eq__(self, other):
        if (self.characteristic != other.characteristic):
            raise ValueError("Characteristics don't match")
        else:
            if (self.value == other.value):
                return True
            else:
                return False

a = RingInt(5,7)
b = RingInt(5,6)
print(a, b, a==b)
