#################### Using List comprehension but using def ####################
# def collapse(L):
#     if isinstance(L, list) and L:
#         return ' '.join([collapse(elem) for elem in L])
#     else:
#         return L
################################################################################

################### Using List comprehension and using lambda ##################
# collapse = lambda l: " ".join([collapse(elem) for elem in l]) if (isinstance(l, list) and l) else '' if l == [] else l
################################################################################

################ Without using List comprehension but using def ################
# def collapse(l):
#     if isinstance(l, list) and l:
#         return " ".join((collapse(l[:-1]) + ' ' + collapse(l.pop())).split())
#     elif l == []:
#         return ''
#     else:
#         return l
################################################################################

############## Without using List comprehension and using lambda ###############
# collapse = lambda l: (collapse(l[:-1]) + " " + collapse(l.pop())) if (isinstance(l, list) and l) else '' if l == [] else l
collapse = lambda l: ' '.join((collapse(l[:-1]) + ' ' + collapse(l.pop())).split()) if (isinstance(l, list) and l) else '' if l == [] else l
################################################################################

# Tests
# x = [["ab"], ["ac", ["ad", ["ae", "aas"]]], ["af"]]
# y = [[[[[['b', '', 'a']]], ['asd']]]]
# print(collapse(x))
# print(collapse(y))
