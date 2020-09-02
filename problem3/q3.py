import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--candies",  "-ca", type=str, required=True)
parser.add_argument("--children", "-ch", type=str, required=True)

args = parser.parse_args()
cafile  = args.candies
chfile = args.children

with open(cafile, 'r') as f:
    m = int(f.readline().split()[0]) # no. of candies
    candies = f.readline().split() # list of candies
    candies = list(map(int, candies)) # convert all to int

with open(chfile, 'r') as f:
    n = int(f.readline().split()[0])
    capr = [list(map(int,f.readline().split())) for _ in range(n)] # contains candy,price pairs

capr.sort(key=lambda x:x[1], reverse=True) # sort according to the price offered

amount = 0
for c in capr:
    if c[0] in candies:
        amount += c[1]
        candies.remove(c[0]) # sold!

print(amount)