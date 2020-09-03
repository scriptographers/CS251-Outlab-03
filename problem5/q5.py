# Enter your code here

def rotate(m):
    temp = []
    for i in range(0, len(m), 1):
        temp.append([m[j][i] for j in range(len(m) - 1, -1, -1)])
    return temp
