def smallest(list):
    if len(list) == 1:
        return list[0]
    if list[1] < list[0]:
        list.pop(0)
    else:
        list.pop(1)
    return smallest(list)

def main():
    print(smallest([6,5,1,3,4]))
    print(smallest([6,5,11,3,4]))
    print(smallest([6,15,11,13,14]))
    print(smallest([2,15,11,13,4]))

if __name__ == '__main__':
    main()