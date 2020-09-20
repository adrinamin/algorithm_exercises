import sys


def maxProduct(xs):

    max_prod = 0
    xs_neg = []
    
    for panel in xs:
        if panel < 0:
            xs_neg.append(panel)
            continue

        if panel != 0:
            if max_prod == 0:
                max_prod = 1
            max_prod *= panel
            continue

    if len(xs_neg) != 0:
        xs_neg_sorted = count_sort(xs_neg)
        if len(xs_neg_sorted) % 2 != 0:
            maximum_negativ = int(max(xs_neg_sorted))
            xs_neg_sorted.remove(maximum_negativ)   

        for p in xs_neg_sorted:
            if max_prod == 0:
                max_prod = 1
            max_prod *= p

    return str(max_prod)


def count_sort(arr):
    maximum = int(max(arr))
    minimum = int(min(arr))
    length = maximum - minimum + 1

    count_arr = [0 for _ in range(length)]
    output_arr = [0 for _ in range(len(arr))]

    for i in range(len(arr)):
        count_arr[arr[i]-minimum] += 1
   
    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i-1]

    for i in range(len(arr)-1, -1, -1):
        output_arr[count_arr[arr[i]-minimum] -1] = arr[i]
        count_arr[arr[i] - minimum] -= 1

    for i in range(0, len(arr)):
        arr[i] = output_arr[i]

    return arr


def main(arr: []):
    maxProduct(arr)
    

if __name__ == '__main__':
    main(sys.argv[1])