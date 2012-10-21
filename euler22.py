def euler22():
    total_sum = 0
    name_file = open("names.txt", "r")
    name_list = sorted(name_file.read().replace('"',"").split(","))
    for j, name in enumerate(name_list):
        name_sum = 0
        for letter in name:
            # Sum the letters in the name (only big letters)
            name_sum += ord(letter)-64
        # Add the position in the list to the sum
        total_sum = total_sum + (name_sum * (j + 1))
        print name + "   " + str(name_sum) + "  " + str(total_sum)

    print total_sum
        
#    print name_list
def main():
    euler22()

if __name__ == "__main__":
    main()
