collapse = lambda l: ' '.join((collapse(l[:-1]) + ' ' + collapse(l.pop())).split()) if (isinstance(l, list) and l) else '' if l == [] else l
