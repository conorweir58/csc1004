def biggest(list):
    if len(list) == 1:
        return list[0]
    if list[0] < list[1]:
        list.pop(0)
    else:
        list.pop(1)
    return biggest(list)