def reverse(list, list2=None):
    if list2 == None:
        list2 = []
    if len(list) == 0:
        return list2
    if 0 < len(list):
        list2.append(list.pop())
    return reverse(list, list2)


def main():
    print(reverse([1,2,3]))
    print(reverse([3,4,5,6]))
    print(reverse([1,2]))

if __name__ == '__main__':
    main()