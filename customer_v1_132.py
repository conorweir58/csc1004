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

def main():
    c1 = Customer('Alan Wren', 12434655, 100.00)
    c2 = Customer('John Squire', 54211677, 200.22)
    c3 = Customer('Ian Brown', 89766121)

    assert(c1.name == 'Alan Wren')
    assert(c1.number == 12434655)
    assert(c1.balance == 100.00)

    print(c1)
    print(c2)
    print(c3)

if __name__ == '__main__':
    main()