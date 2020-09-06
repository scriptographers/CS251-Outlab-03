from ring import RingInt


class Series:

    def __init__(self, k, x, n):
        k, x, n = int(k), int(x), int(n)
        self.k, self.n = k, n
        self.X = RingInt(x, n)
        self.I = RingInt(0, n)
        self.N = RingInt(1, n)  # N stands for next

    def __iter__(self):
        return self

    def __next__(self):
        if self.I.value >= self.k:
            raise StopIteration
        else:
            self.I.value += 1
            P = self.N  # P stands for previous
            self.N *= (self.X / self.I)
            return P


if __name__ == "__main__":
    in_str = str(input())
    in_list = in_str.split(' ')
    k, x, n = in_list[0], in_list[1], in_list[2]

    for ele in Series(k, x, n):
        print(ele)
