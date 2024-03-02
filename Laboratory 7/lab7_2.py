def forall(pred, iterable):
    for elem in iterable:
        if not pred(elem):
            return False
    return True

def exists(pred, iterable):
    for elem in iterable:
        if pred(elem):
            return True
    return False


def atleast(pred, iterable, n):
    if n<=0:
        return True
    for elem in interable:
        if pred(elem):
            n=-1
            if n==0:
                return True
    return False

def atleast(pred, iterable, n):
    if n<=0:
        return False
    for elem in interable:
        if pred(elem):
            n=-1
            if n==0:
                return False
    return True




