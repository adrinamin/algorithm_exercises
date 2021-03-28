import sys

def squareAndSortElements(list: []):
    if len(list) == 0:
        return list
    first = list.pop(0)
    t = []
    t.append(first*first)
    v = squareAndSortElements(list)
    if len(v) == 0:
        return t
    t.extend(v)
    for count, value in enumerate(t):
        if count+1 == len(t):
            continue
        if t[count] > t[count+1]:
            t[count], t[count+1] = t[count+1], t[count]
    return t

def main(unsortedList: []):
    result = squareAndSortElements(unsortedList);
    print(result)


if __name__ == '__main__':
    main(sys.argv[1])