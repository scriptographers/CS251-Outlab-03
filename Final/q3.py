from collections import Counter, defaultdict
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--candies", "-ca", type=str, required=True)
parser.add_argument("--children", "-ch", type=str, required=True)

args = parser.parse_args()
cafile = args.candies
chfile = args.children

with open(cafile, 'r') as f:
    m = int(f.readline().split()[0])  # no. of candies
    candies = f.readline().split()  # list of candies
    candies = list(map(int, candies))  # convert all to int
    candies = Counter(list(map(int, candies)))  # Made a counter

with open(chfile, 'r') as f:
    n = int(f.readline().split()[0])
    capr = [list(map(int, f.readline().split())) for _ in range(n)]  # contains candy,price pairs
    capr_ = defaultdict(list)
    for k, v in capr:
        capr_[k].append(v)

amount = 0
for c, cnt in candies.items():
    capr_[c].sort(reverse=True)
    for i in range(0, min(cnt, len(capr_[c]))):
        amount += capr_[c][i]

print(amount)
