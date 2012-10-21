def euler21():
    MAX_NO = 10000
    ambicle_total = 0
    number_list = range(2,MAX_NO)
    position = 0
    while(True):
        try:
            sum_1 = sum(get_divisors(number_list[position]))
        except IndexError:
            break

        sum_2 = sum(get_divisors(sum_1))
        
        if ((sum_2 == number_list[position]) and (sum_2 <= MAX_NO) and (not number_list[position] == sum_1)):
            print number_list[position]
            print sum_1
            print sum_2
            ambicle_total += number_list[position] + sum_1
            number_list.remove(sum_1)

        position += 1

    print ambicle_total

        
def get_divisors(number):
    divisor_list = []
    for div in range(1,(number/2)+1):
        if number%div == 0:
            divisor_list.append(div)

    return divisor_list

def main():
    euler21()

if __name__ == "__main__":
    main()
