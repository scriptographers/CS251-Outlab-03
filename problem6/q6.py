# Enter your code here

# def collapse(L):
#     if isinstance(L, list) and L:
#         return ' '.join([collapse(L.pop()), collapse(L)])
#     else:
#         return L

# collapse = lambda l: ' '.join([collapse(l.()),]) if isinstance(l, list) else l
# collapse = lambda l: ' '.join(reversed([collapse(l.pop()), collapse(l)])) if (isinstance(l, list) and l) else '' if isinstance(l, list) else l

# def collapse(l):
#     if isinstance(l, list) and l:
#         return " ".join((collapse(l[:-1]) + ' ' + collapse(l.pop())).split())
#     elif l == []:
#         return ''
#     else:
#         return l

collapse = lambda l: " ".join((collapse(l[:-1]) + ' ' + collapse(l.pop())).split()) if (isinstance(l, list) and l) else '' if l == [] else l

x = [["ab"], ["ac", ["ad", ["ae"]]], ["af"]]
print(collapse(x))
