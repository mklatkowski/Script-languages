
def acronym(words):
    return ''.join(list(map(lambda x: x[0], words)))

def median(values):
    return (values[0]+values[-1])/2 if len(values)<=2 else median(sorted(values)[1:-1])


def pierwiastek(x, epsilon=0.1):
    def netwon_iter(y):
        return (y + x / y) / 2

    def within_eps(y):
        return abs(y ** 2 - x) < epsilon

    def sqrt_iter(y):
        return y if within_eps(y) else sqrt_iter(netwon_iter(y))

    return sqrt_iter(1.0)


def make_alpha_dict(text):
    words = text.split()
    letters = set(filter(str.isalpha, text))
    return {letter: [word for word in words if letter in word] for letter in letters}

def flatten(not_flat_list):
    def flatten_in(not_flat_list, flat_list):
        match not_flat_list:
            case []:
                return flat_list
            case [head, *tail]:
                return flatten_in(tail, flat_list+flatten_in(head, []))
            case x:
                return [x]
    return flatten_in(not_flat_list, [])
