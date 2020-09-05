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


a = RingInt(5,7)
b = RingInt(4,7)
print(a, b, a-b*a)
