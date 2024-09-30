from math import sqrt

class Stack(object):

    def __init__(self):
        self.l = []

    def push(self, e):
        self.l.append(e)

    def pop(self):
        return self.l.pop()

    def top(self):
        return self.l[-1]

    def is_empty(self):
        return len(self.l) == 0

    def __len__(self):
        return len(self)

def calculator(test):

    binops = {'+': float.__add__,
    '-': float.__sub__,
    '*': float.__mul__,
    '/': float.__truediv__}

    uniops = {'n': float.__neg__,
    'r': sqrt}

    s = Stack()

    test = test.split()
    for c in test:
        if c in binops:
            n2 = float(s.pop())
            n1 = float(s.pop())
            s.push(binops[c](n1, n2))
        elif c in uniops:
            n = float(s.pop())
            s.push(uniops[c](n))
        else:
            s.push(c)

    return float(s.pop())

tests = ['5',
'8.5 2 /',
'2 3 +',
'2 3 r +',
'1 2 3 * +',
'5 2 n *',
'1 2 3 + -',
'2 1 2 3 + - *',
'2 1 2 3 + - * n',
'2 1 2 3 + - * n r',
'6 +',
'9 r']

def main():

    for test in tests:
        try:
            a = calculator(test.strip())
            print('{:.2f}'.format(a))
        except IndexError:
            print('Invalid RPN expression')

if __name__ == '__main__':
    main()
            
