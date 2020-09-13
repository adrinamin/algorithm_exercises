import sys


def get_minion_id(i):
    primenumbers = ""
    minion_id = ""
    lower = 0
    upper = 21000 # accumulates 10375 digits > 10000 minions
    
    # Sieve of Eratosthenes Method
    # boolean array with all elements set to True
    prime = [True for element in range(upper+1)] 
    p=2 # first prime number
    
    # count up increments of p until reaching upper
    while p*p <=upper:
        if (prime[p] == True):
            # mark number with False if not prime
            for num in range(p*p, upper+1, p):
                prime[num] = False
        p+=1
    
    # iterate over all numbers from 2 to upper
    # and if prime == True, accumulate string
    for j in range(2,upper):
        if prime[j]:
            primenumbers = primenumbers + str(j)
    
    end = i+5         
    minion_id = primenumbers[i:end]
    return minion_id


def main(i):
    get_minion_id(i)

if __name__ == '__main__':
    main(sys.argv[0])