def is_prime(n):
    for i in range(2, n):
        if (n % i == 0):
            return False
    return True


def f2c(deg):
    return (deg-32)*5/9


def printTable():
    for i in range(0, 101, 10):
        print


def letter_count(string):
    return {l: string.count(l) for l in set(string)}


def main():
    print(letter_count("a rose is a rose is a rose"))


main()
