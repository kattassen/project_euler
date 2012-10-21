def euler22():
    MAX_NO = 22000
    abundant_even = []
    abundant_odd = []
    integer_list = [1,2,3,4,5,6,7,8,9,10,11]
    for i in range(12,MAX_NO+1):
        if sum(get_divisors(i)) > i:
            if not i%2 == 0:
                abundant_odd.append(i)
            else:
                abundant_even.append(i)

        if i%2 == 0:
            list_1 = abundant_even + abundant_odd
            list_2 = abundant_even + abundant_odd
        else:
            list_1 = abundant_even
            list_2 = abundant_odd


        # Check if this number can be the sum of two abundant numbers
        stop = False
#        loop_cnt = 0
        for x in list_1:
#            print "X  " + str(x) + "   " + str(i)
            if (i < 955 and not i%2 == 0):
                 break
            for y in reversed(list_2):
#                print "Y  " + str(y)
#                loop_cnt += 1
                if x + y == i:
                    stop = True
#                    print str(x) + " + " + str(y) + " = " + str(i)
                    break
                
            if stop == True:
                break
#        print str(i) + "  Loops" + str(loop_cnt)
        if stop == False:
            integer_list.append(i)

    print sum(integer_list)


def get_divisors(number):
    divisor_list = []
    for div in range(1,(number/2)+1):
        if number%div == 0:
            divisor_list.append(div)

    return divisor_list

def main():
    euler22()

if __name__ == "__main__":
#    import cProfile
#    cProfile.run('main()')
    main()
