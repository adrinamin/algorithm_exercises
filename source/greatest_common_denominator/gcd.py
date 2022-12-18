import math

def get_greatest_common_denominator(x, y):
        while(y):
            x, y = y, x % y
        return x

def main():
    l = [9, 6, 15, 21, 33]
    num1=l[0]
    num2=l[1]
    gcd = get_greatest_common_denominator(num1, num2)
    
    for i in range(2,len(l)):
        gcd = get_greatest_common_denominator(gcd, l[i])

if __name__ == "__main__":
    main()