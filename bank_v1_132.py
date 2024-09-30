class Customer(object):

    def __init__(self, name, number, balance=0):
        self.name = name
        self.number = number
        self.balance = balance
    
    def __str__(self):
        output = []
        output.append('Name: {}'.format(self.name))
        output.append('Number: {}'.format(self.number))
        output.append('Balance: {:.2f}'.format(self.balance))
        return '\n'.join(output)

class Bank(object):

    def __init__(self):
        self.bank = {}
    
    def add(self, c):
        self.bank[c.number] = c
    
    def remove(self, number):
        del(self.bank[number])
    
    def lookup(self, number):
        if number in self.bank:
            return self.bank[number]

def main():
    c1 = Customer('Alan Wren', 12434655, 100.00)
    c2 = Customer('John Squire', 54211677, 200.22)

    b = Bank()

    b.add(c1)
    b.add(c2)

    c = b.lookup(12434655)
    assert(isinstance(c, Customer))
    assert(c.name == 'Alan Wren')
    assert(c.number == 12434655)
    assert(c.balance == 100.00)

    b.remove(12434655)
    c = b.lookup(12434655)
    assert(c is None)

if __name__ == '__main__':
    main()
