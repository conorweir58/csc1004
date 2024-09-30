class Customer(object):

    def __init__(self, name, number, balance=0):
        self.name = name
        self.number = number
        self.balance = balance
    
    def lodge(self, lodgment):
        self.balance += lodgment
    
    def withdraw(self, withdrawl):
        if withdrawl < self.balance:
            self.balance -= withdrawl
    
    def __str__(self):
        output = []
        output.append('Name: {}'.format(self.name))
        output.append('Number: {}'.format(self.number))
        output.append('Balance: {:.2f}'.format(self.balance))
        return '\n'.join(output)

def main():
    c1 = Customer('Alan Wren', 12434655, 100.00)

    c1.lodge(1.11)
    print(c1)

    c1.withdraw(200)
    print(c1)

    c1.withdraw(2)
    print(c1)

if __name__ == '__main__':
    main()