from decimal import *
def euler_26():
    getcontext().prec = 4000

    high_count = 0
    for i in range(2,1000):
        decimals = str(Decimal(1)/Decimal(i))[2:-1].lstrip('0')
        serie = []

        for char in decimals:
            serie.append(char)

            # Start with search of string until string is longer than 5
            if len(serie) > 5:
                if decimals[len(serie):len(serie)*2] == "".join(serie):
                    print "Reacurrence!!!! d = " + str(i) + "  " + str(len(serie))
                    if len(serie) > high_count:
                        high_count = len(serie)
                    break

    print high_count

def main():
    euler_26()

if __name__ == "__main__":
    main()
