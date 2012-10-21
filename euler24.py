import itertools
def euler24():
    chars = ["0","1","2","3","4","5","6","7","8","9"]
    combinations = []

    for x in itertools.permutations(chars,10):
        combinations.append(x)

    print "".join(combinations[999999])

def main():
    euler24()

if __name__ == "__main__":
#    import cProfile
#    cProfile.run('main()')
    main()
