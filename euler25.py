def euler_25():
    x = y =1
    loop_count = 2
    while True:
        loop_count += 1
        z = x + y
        y = x
        x = z
        if len(str(z)) == 1000:
            break

    print loop_count

def main():
    euler_25()

if __name__ == "__main__":
    main()
