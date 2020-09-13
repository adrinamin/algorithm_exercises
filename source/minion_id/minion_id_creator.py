import sys


def get_minion_id(i):
    primenumbers = ""
    minion_id = ""
    lower = 0
    upper = 1000
    for num in range(lower, upper + 5):
        if num > 1:
            for j in range(2,num):
                if (num%j) == 0:
                    break
            else:
                primenumbers = primenumbers + str(num)
              
    minion_id = primenumbers[i:i+5]
    return minion_id


def main(i):
    get_minion_id(i)

if __name__ == '__main__':
    main(sys.argv[0])