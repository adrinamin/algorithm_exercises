import random as r


def rand7():
    tmp = r.randint(1,7)
    return tmp%7+1

def rand5():
    return r.randint(1,7)%5+1

def main():
    return rand7()


if __name__ == '__main__':
    for i in range(10):
        print(main())