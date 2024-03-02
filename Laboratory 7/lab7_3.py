import random
import string

class PasswordGenerator:
    def __init__(self, length, charset=string.ascii_letters + string.digits, count=float("inf")):
        self.length = length
        self.charset = ''.join(charset)
        self.total_count = count
        self.generated_count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.generated_count < self.total_count:
            password = ''.join(random.choice(self.charset) for _ in range(self.length))
            self.generated_count += 1
            return password
        raise StopIteration

if __name__ == '__main__':
    number_of_passwords = 5
    pass_gen = PasswordGenerator(5, count=number_of_passwords)
    it = iter(pass_gen)

    for _ in range(number_of_passwords):
        print(next(it))
