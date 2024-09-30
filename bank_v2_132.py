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

    def __gt__(self, other):
        return other.number < self.number

class Bank(object):

    def __init__(self):
        self.bank = {}
    
    def add(self, c):
        self.bank[c.number] = c
    
    def remove(self, number):
        del(self.bank[number])
    
    def total_funds(self):
        self.total = 0
        for number in self.bank:
            self.total += self.bank[number].balance
        return self.total
    
    def lookup(self, number):
        if number in self.bank:
            return self.bank[number]
    
    def __str__(self):
        output = ['{}'.format(c) for c in sorted(self.bank.values())]
        output.append('Total funds: {:.2f}'.format(self.total_funds()))
        return '\n'.join(output)
    

def main():
    c1 = Customer('Alan Wren', 12434655, 100.00)
    c2 = Customer('John Squire', 54211677, 200.22)
    c3 = Customer('Ian Brown', 10145211, 1.50)

    b = Bank()

    b.add(c1)
    b.add(c2)
    b.add(c3)

    print(b)

if __name__ == '__main__':
    main()