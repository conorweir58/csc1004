def collatz(n):
    print(n)
    if n == 1:
        return 1
    if n % 2:
        n = (n * 3) + 1
    else:
        n = n // 2
    return collatz(n)




def main():
    collatz(5)

if __name__ == '__main__':
    main()