
import math


def euler_6():
    numbers = 1000

    sum_1 = 0
    sum_2 = 0
    for i in range(1,numbers + 1):
        sum_1 = sum_1 + i*i
        sum_2 = sum_2 + i

    print sum_2*sum_2-sum_1


def euler_7():
    steps = 100
    intervall = 1100
    results = [2]
    for i in range(0,steps):
        for j in range(1,intervall,2):
            for x in range(1,int(math.sqrt(j+i*intervall))+1,2):
                if (((j+i*intervall) % x ==  0) and not x == 1) or j+i*intervall == 1:
                    break
                elif x >= int(math.sqrt(j+i*intervall))-1:
                    results.append(j+i*intervall)

    print results[10000]

             
def euler_8():
    nums = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"

    all_sums = []
    sums = [1,1,1,1,1]

    for i in range(0,len(nums)):
        # Add numbers one by one to sums

        if i % 5 == 0:
            all_sums.append(sums[0])
            sums[0] = 1
        elif (i-1) % 5 == 0:
            all_sums.append(sums[1])
            sums[1] = 1
        elif (i-2) % 5 == 0:
            all_sums.append(sums[2])
            sums[2] = 1
        elif (i-3) % 5 == 0:
            all_sums.append(sums[3])
            sums[3] = 1
        elif (i-4) % 5 == 0:
            all_sums.append(sums[4])
            sums[4] = 1
            
        sums[0] = int(nums[i]) + sums[0]

        if i > 0:
            sums[1] = int(nums[i]) * sums[1]
        if i > 1:
            sums[2] = int(nums[i]) * sums[2]
        if i > 2:
            sums[3] = int(nums[i]) * sums[3]
        if i > 3:
            sums[4] = int(nums[i]) * sums[4]

    print all_sums
    print max(all_sums)


def euler_9():
    a_max = 250
    b_max = 350

    for a in range(1,a_max):
        for b in range(a+1, a_max+b_max):
            for c in range(b+1, 1001):
                if (a+b+c) == 1000:
                    if (a*a + b*b) == c*c:
                        print str(a) + " " + str(b) + " " + str(c)
                        print a*b*c


def euler_10():
    steps = 1000
    intervall = 2100
    prime_sum = 2
    for i in range(0,steps):
        for j in range(1,intervall,2):
            for x in range(1,int(math.sqrt(j+i*intervall))+1,2):
                if (((j+i*intervall) % x ==  0) and not x == 1) or j+i*intervall == 1:
                    break
                elif x >= int(math.sqrt(j+i*intervall))-1:
                    if j+i*intervall >= 2000000:
                        print "prime_sum = "
                        print prime_sum
                        print j+i*intervall
                        exit()
                        
                    prime_sum = prime_sum + j+i*intervall

def euler_11():    
    number_string = """08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48"""

    number_grid = number_string.split('\n')
    for i in range(0,len(number_grid)):
        number_grid[i] = number_grid[i].split(' ')


    product_max = 0
    numbers = [1,1,1,1]

    # Loop each row in grid
    for row in range(0,len(number_grid)):
        # Loop each number in row until len -4
        for col in range(0,len(number_grid[0])-4):
            # Calculate row poducts
            if col >= 3:
                temp_product = int(number_grid[row][col])*int(number_grid[row][col-1])*int(number_grid[row][col-2])*int(number_grid[row][col-3])
                if temp_product > product_max:
                    product_max = temp_product
            

                if row >= 3:
                    temp_product = int(number_grid[row][col])*int(number_grid[row-1][col-1])*int(number_grid[row-2][col-2])*int(number_grid[row-2][col-3])
                    if temp_product > product_max:
                        product_max = temp_product

                if row < 17:
                    temp_product = int(number_grid[row][col])*int(number_grid[row+1][col-1])*int(number_grid[row+2][col-2])*int(number_grid[row+3][col-3])
                    if temp_product > product_max:
                        product_max = temp_product                   

            # Calculate column products
            if row >= 3:
                temp_product = int(number_grid[row][col])*int(number_grid[row-1][col])*int(number_grid[row-2][col])*int(number_grid[row-3][col])
                if temp_product > product_max:
                    product_max = temp_product
            
    print product_max

def euler_12():
    # This is a bad solution... it takes forever to get to the correct number.
    # To shorten the run I have started from a higer number (from earlier run)
    triangle = 48565440
    max_divisors = 1
    for i in range(9855+1,13000):
        triangle = triangle + i
        
        if not triangle % 10 == 0:
            continue
        # Start with 2 diviors (1 and the number itself)
        # and only divide up to half the number
        divisors = 2
        for j in range(2, triangle/2+1):
            if triangle % j == 0:
                divisors = divisors + 1
                
        if divisors > max_divisors:
            max_divisors = divisors
            
            print i
            print triangle
            print max_divisors
            if max_divisors > 500:
                exit()

def euler_13():
    numbers = """37107287533902102798797998220837590246510135740250
46376937677490009712648124896970078050417018260538
74324986199524741059474233309513058123726617309629
91942213363574161572522430563301811072406154908250
23067588207539346171171980310421047513778063246676
89261670696623633820136378418383684178734361726757
28112879812849979408065481931592621691275889832738
44274228917432520321923589422876796487670272189318
47451445736001306439091167216856844588711603153276
70386486105843025439939619828917593665686757934951
62176457141856560629502157223196586755079324193331
64906352462741904929101432445813822663347944758178
92575867718337217661963751590579239728245598838407
58203565325359399008402633568948830189458628227828
80181199384826282014278194139940567587151170094390
35398664372827112653829987240784473053190104293586
86515506006295864861532075273371959191420517255829
71693888707715466499115593487603532921714970056938
54370070576826684624621495650076471787294438377604
53282654108756828443191190634694037855217779295145
36123272525000296071075082563815656710885258350721
45876576172410976447339110607218265236877223636045
17423706905851860660448207621209813287860733969412
81142660418086830619328460811191061556940512689692
51934325451728388641918047049293215058642563049483
62467221648435076201727918039944693004732956340691
15732444386908125794514089057706229429197107928209
55037687525678773091862540744969844508330393682126
18336384825330154686196124348767681297534375946515
80386287592878490201521685554828717201219257766954
78182833757993103614740356856449095527097864797581
16726320100436897842553539920931837441497806860984
48403098129077791799088218795327364475675590848030
87086987551392711854517078544161852424320693150332
59959406895756536782107074926966537676326235447210
69793950679652694742597709739166693763042633987085
41052684708299085211399427365734116182760315001271
65378607361501080857009149939512557028198746004375
35829035317434717326932123578154982629742552737307
94953759765105305946966067683156574377167401875275
88902802571733229619176668713819931811048770190271
25267680276078003013678680992525463401061632866526
36270218540497705585629946580636237993140746255962
24074486908231174977792365466257246923322810917141
91430288197103288597806669760892938638285025333403
34413065578016127815921815005561868836468420090470
23053081172816430487623791969842487255036638784583
11487696932154902810424020138335124462181441773470
63783299490636259666498587618221225225512486764533
67720186971698544312419572409913959008952310058822
95548255300263520781532296796249481641953868218774
76085327132285723110424803456124867697064507995236
37774242535411291684276865538926205024910326572967
23701913275725675285653248258265463092207058596522
29798860272258331913126375147341994889534765745501
18495701454879288984856827726077713721403798879715
38298203783031473527721580348144513491373226651381
34829543829199918180278916522431027392251122869539
40957953066405232632538044100059654939159879593635
29746152185502371307642255121183693803580388584903
41698116222072977186158236678424689157993532961922
62467957194401269043877107275048102390895523597457
23189706772547915061505504953922979530901129967519
86188088225875314529584099251203829009407770775672
11306739708304724483816533873502340845647058077308
82959174767140363198008187129011875491310547126581
97623331044818386269515456334926366572897563400500
42846280183517070527831839425882145521227251250327
55121603546981200581762165212827652751691296897789
32238195734329339946437501907836945765883352399886
75506164965184775180738168837861091527357929701337
62177842752192623401942399639168044983993173312731
32924185707147349566916674687634660915035914677504
99518671430235219628894890102423325116913619626622
73267460800591547471830798392868535206946944540724
76841822524674417161514036427982273348055556214818
97142617910342598647204516893989422179826088076852
87783646182799346313767754307809363333018982642090
10848802521674670883215120185883543223812876952786
71329612474782464538636993009049310363619763878039
62184073572399794223406235393808339651327408011116
66627891981488087797941876876144230030984490851411
60661826293682836764744779239180335110989069790714
85786944089552990653640447425576083659976645795096
66024396409905389607120198219976047599490197230297
64913982680032973156037120041377903785566085089252
16730939319872750275468906903707539413042652315011
94809377245048795150954100921645863754710598436791
78639167021187492431995700641917969777599028300699
15368713711936614952811305876380278410754449733078
40789923115535562561142322423255033685442488917353
44889911501440648020369068063960672322193204149535
41503128880339536053299340368006977710650566631954
81234880673210146739058568557934581403627822703280
82616570773948327592232845941706525094512325230608
22918802058777319719839450180888072429661980811197
77158542502016545090413245809786882778948721859617
72107838435069186155435662884062257473692284509516
20849603980134001723930671666823555245252804609722
53503534226472524250874054075591789781264330331690""".split('\n')

    sum = 0
    for i in numbers:
        sum = sum + int(i)

    print sum
        
def euler_14():

    max_count = 0
    for start_number in range(1,1000000):
        n = start_number
        stop = False
        count = 1
        while (not stop == True):
            count = count + 1
            if n % 2 == 0:
                n = n/2
            else:
                n = 3 * n + 1

            if n == 1:
                stop = True

        if count > max_count:
            max_count = count
            n_max = start_number

            print n_max
            print max_count


x_dim = 20
y_dim = 20
branches = 0
def euler_15():
    global branches

#    stop = False
#    while(not stop):
#        # Start with x ==1, we multiply later the result
#        traverse_tree(1,0)
#        stop = True
#        print branches*2

    triangle = [[1]]
    # Loop rows in triangle
    for row in range(1,41):
        # Add a 1 in the first position
        triangle.append([1])

        for col in range(0,row):
            if col == row-1:
                triangle[row].append(1)
            else:
                number = triangle[row-1][col] + triangle[row-1][col+1]
                triangle[row].append(number)

    for row in triangle:
        print max(row)

def traverse_tree(x,y):
    global branches
    global x_dim
    global y_dim
    if branches%1000000 == 0:
        print branches
    branches_start = branches
    # Are we at the bottom?
    if x == x_dim and y == y_dim:
        branches = branches + 1
    
    # First go right if possible
    if x < x_dim:
        traverse_tree(x+1,y)

        # If we are on a "symetric" coordinate, just do one
        # search and double it.
        if x == y:
            branches = branches+(branches-branches_start)
            return

    if y < y_dim:
        traverse_tree(x,y+1)    


def euler_16():
    x = 2**1000

    total = 0
    for i in range(0,len(str(x))):
        total = x%10 + total
        x = x/10
    print total

def euler_17():
    numbers = {1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine', 10:'ten', 11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen', 20:'twenty', 30:'thirty', 40:'forty', 50:'fifty', 60:'sixty', 70:'seventy', 80:'eighty', 90:'ninety', 100:'hundred'}

    letters = 0
    number_string = ""
    for i in range(1,1000):
        number_string = ""
        # Add hundreds numbers
        if i > 99:
            number_string += numbers[int(str(i)[-3])]
            number_string += "hundred"
            if not i % 100 == 0:
                number_string += "and"

        if 0 < int(str(i)[-2:]) < 20:
            number_string += numbers[int(str(i)[-2:])]
        else:
            if not str(i)[-2] == '0':
                # Add tenth numbers
                number_string += numbers[int(str(i)[-2])*10]
            if not str(i)[-1] == '0':
                # Add oneth numbers
                number_string += numbers[int(str(i)[-1])]
#        print number_string
        letters += len(number_string)

    letters += len("onethousand")
    print letters
        
def euler_19():
    tot = 1
    for i in range(1,101):
        tot = tot * i

    sum_tot = 0
    for x in str(tot):
        sum_tot += int(x)

    print sum_tot


def main():
#    euler_6()
#    euler_7()
#    euler_8()
#    euler_9()
#    euler_10()
#    euler_11()
#    euler_12()
#    euler_13()
#    euler_14()
#    euler_15()
#    euler_16()
#    euler_17()
    euler_19()

if __name__ == "__main__":
    main()
