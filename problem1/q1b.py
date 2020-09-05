import re
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--message",  "-m", type=str, required=True)

args = parser.parse_args()
infile = args.message

with open(infile, 'r') as f:
    n = int(f.readline().split()[0])
    message = f.read()

# Checks whether a string is an integer or not
def isInt(s):
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    return s.isdigit()

extract_numbers = re.compile("(?:[0-9]+)(?:,[0-9]+)+") # Extracts the comma separated ints from the code
def check_code(code):
    ab = extract_numbers.findall(code)
    if (len(ab) == 2):
        a = ab[0].split(',')
        b = ab[1].split(',')
        if ((len(a) == 0) or (len(b) == 0)):
            return False
    else:
        return False

    sum_a = 0
    for i in range(len(a)):
        if isInt(a[i]):
            if ((int(a[i]) < n) and (int(a[i]) >= 0)):
                sum_a += (i+1)*int(a[i])
            else:
                return False
        else:
            return False

    sum_b = 0
    for i in range(len(b)):
        if isInt(b[i]):
            if ((int(b[i]) < n) and (int(b[i]) >= 0)):
                sum_b += (i+1)*int(b[i])
            else:
                return False
        else:
            return False

    if ((sum_a%n != 0) or (sum_b%n != 0)):
        return False

    return True

extract_code = re.compile(r"\$\((?:[0-9]+)(?:,[0-9]+)+\)\#\((?:[0-9]+)(?:,[0-9]+)+\)\$")
matches = extract_code.findall(message)
# print(matches)
is_corrupt = False
for match in matches:
    if not check_code(match):
        is_corrupt = True
        print("CORRUPTED")
        break
if not is_corrupt:
    print("OK")