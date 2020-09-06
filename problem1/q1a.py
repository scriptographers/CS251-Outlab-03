import argparse
from ring import *

parser = argparse.ArgumentParser()
parser.add_argument("--input",  "-inp", type=str, required=True)
parser.add_argument("--output", "-out", type=str, required=True)

args = parser.parse_args()
infile  = args.input
outfile = args.output

# Returns (i!)
def factorial(i):
    f = RingInt(1, i.characteristic)
    temp_i = RingInt(i.value, i.characteristic)
    while (temp_i.value > 0):
        f = f*temp_i
        temp_i.value -= 1
    return f

# Returns nCr
def combinations(n, r):
    numer = factorial(n)
    denom = factorial(n-r)*factorial(r)
    return (numer/denom)

def series1(k, x, n):
    try:
        S = RingInt(0, n)
        X = RingInt(x, n)
        I = RingInt(0, n)
        for i in range(k):
            I.value = i
            S += (X**I.value)/(factorial(I))
        return S
    except ValueError:
        return "UNDEFINED"

def series2(k, x, n):
    try:
        S = RingInt(1, n)
        X = RingInt(x, n)
        I = RingInt(0, n)
        J = RingInt(0, n)
        temp = RingInt(0, n)
        for i in range(k):
            I.value = i
            J.value = 0
            temp.value = 0
            for j in range(i+1):
                J.value = j
                temp += combinations(X, J)
            S *= temp
            X.value += 1
        return S
    except ValueError:
        return "UNDEFINED"

def series3(k, x, n):
    try: 
        S = RingInt(0, n)
        I = RingInt(1, n)
        for i in range(1, k+1):
            I.value = i
            S += I**x
        return S
    except ValueError:
        return "UNDEFINED"

def solve(k, x, n, s_no):
    if (s_no == 1):
        return series1(k, x, n)
    elif (s_no == 2):
        return series2(k, x, n)
    elif (s_no == 3):
        return series3(k, x, n)
    else:
        raise ValueError("Series number must be 1, 2 or 3")

# Clear data in output before writing new output
with open(outfile, 'w') as outf:
    outf.seek(0)                      
    outf.truncate()

with open(infile, 'r') as inpf:
    lines = inpf.readlines()
    for line in lines:
        data = line.split()
        k, x, n, s_no = list(map(int, data))
        out = solve(k, x, n, s_no)
        with open(outfile, 'a') as outf:
            outf.write(str(out)+"\n")