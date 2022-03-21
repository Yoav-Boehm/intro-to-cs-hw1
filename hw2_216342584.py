# Skeleton file for HW2 - Spring 2022 - extended intro to CS

# Add your implementation to this file

# you may NOT change the signature of the existing functions.
# you can add new functions if needed.

# Change the name of the file to include your ID number (hw2_ID.py).
import random # loads python's random module in order to use random.random() in question 2


##############
# QUESTION 1 #
##############
#  Q1a
def divisors(n):
    divisors_n = [i for i in range(1, n//2 + 1) if n%i == 0]
    return divisors_n
#  Q1b
def perfect_numbers(n):
    perfect_nums = []
    num = 1
    while len(perfect_nums) < n:
        divisor = divisors(num)
        if sum(divisor) == num:
            perfect_nums.append(num)
        num += 1
    return perfect_nums
#  Q1c
def abundant_density(n):
    abundant_nums = []
    for i in range(1, n + 1):
        divisor = divisors(i)
        if sum(divisor) > i:
            abundant_nums.append(i)
    return len(abundant_nums)/n
#  Q1e
def semi_perfect_4(n):
    divisors_n = divisors(n)
    for i in range(len(divisors_n)):
        for j in range(len(divisors_n)):
            if j != i:
                for k in range(len(divisors_n)):
                    if k != j:
                        for l in range(len(divisors_n)):
                            sum = divisors_n[i] + divisors_n[j] + divisors_n[k] + divisors_n[l]
                            if sum == n:
                                return True
                            else:
                                sum = 0
    return False

##############
# QUESTION 2 #
##############
# Q2a
def coin():
    num = random.random()
    if num < 0.5:
        return False
    else:
        return True

# Q2b
def roll_dice(d):
    rand = random.random()
    for i in range(1, d + 1):
        if rand < i/d:
            return i

# Q2c
def roulette(bet_size, parity):
    result = roll_dice(37) - 1
    if result == 0:
        return 0
    elif (parity == "odd" and result%2 == 1) or (parity == "even" and result%2 == 0):
        return bet_size*2
    else:
        return 0

# Q2d
def roulette_repeat(bet_size, n):
    betting = 0
    total = 0
    for i in range(n):
        par = coin()
        if par == True:
            betting = roulette(bet_size, "even")
        else:
            betting = roulette(bet_size, "odd")
        total += (betting - bet_size)
    return total

# Q2e
def shuffle_list(lst):
    shuffled_list = []
    temp = lst
    for i in range(len(temp)):
        object1 = roll_dice(len(temp)) - 1
        shuffled_list.append(temp[object1])
        temp.pop(object1)
    return shuffled_list

##############
# QUESTION 3 #
##############
# Q3a
def inc(binary):
    binary_copy = binary[::-1]
    carry = 1
    final_bin = ""
    for i in range(len(binary_copy)):
        if binary_copy[i] == "0" and carry == 0:
            final_bin += "0"
        elif binary_copy[i] == "1" and carry == 0:
            final_bin += "1"
        elif binary_copy[i] == "1" and carry == 1:
            final_bin += "0"
            carry = 1
        elif binary_copy[i] == "0" and carry == 1:
            final_bin += "1"
            carry = 0
    if carry == 1:
        final_bin += "1"
    return final_bin[::-1]
# Q3b
def pad_rev_lists(bin1, bin2):
    pass  # replace with your code


def add(bin1, bin2):
    carry = 0
    final_bin = ""
    longer = []
    shorter = []
    if len(bin1) >= len(bin2):
        longer = bin1[::-1]
        shorter = bin2[::-1]
    else:
        longer = bin2[::-1]
        shorter = bin1[::-1]
    for i in range(len(longer)):
        if i >= len(shorter):
            if longer[i] == "0" and carry == 0:
                final_bin += "0"
            elif longer[i] == "1" and carry == 0:
                final_bin += "1"
            elif longer[i] == "1" and carry == 1:
                final_bin += "0"
                carry = 1
            else:
                final_bin += "1"
                carry = 0
        else:
            if shorter[i] == longer[i] == "0" and carry == 0:
                final_bin += "0"
            elif shorter[i] == longer[i] == "0" and carry == 1:
                carry = 0
                final_bin += "1"
            elif shorter[i] == longer[i] == "1" and carry == 0:
                final_bin += "0"
                carry = 1
            elif shorter[i] == longer[i] == "1" and carry == 1:
                final_bin += "1"
            elif shorter[i] != longer[i] and carry == 0:
                final_bin += "1"
            else:
                final_bin += "0"
                carry = 1
    if carry == 1:
        final_bin += "1"
    return final_bin[::-1]
# Q3c
def pow_two(binary, power):
    final_bin = binary
    if binary == "0":
        return "0"
    for i in range(power):
        final_bin += "0"
    return final_bin
# Q3d
def div_two(binary, power):
    final_bin = ""
    if power >= len(binary):
        return "0"
    else:
        for i in range(len(binary) - power):
            final_bin += binary[i]
    return final_bin
# Q3e
def leq(bin1, bin2):
    if len(bin2) > len(bin1):
        return True
    elif len(bin1) > len(bin2):
        return False
    else:
        for i in range(len(bin2)):
            if bin2[i] == bin1[i]:
                continue
            elif bin2[i] == "1" and bin1[i] == "0":
                return True
            elif bin1[i] == "1" and bin2[i] == "0":
                return False
    return True

# Q3f
def to_decimal(binary):
    binary_copy = binary[::-1]
    dec_num = 0
    for i in range(len(binary_copy)):
        if binary_copy[i] == "1":
            dec_num += 2**i
        else:
            continue
    return dec_num


##############
# QUESTION 4 #
##############
# Q4a
def lychrel_loops(n):
    current_num = n
    count = 0
    while True:
        string_n = str(current_num)[::-1]
        current_num += int(string_n)
        count += 1
        if str(current_num) == str(current_num)[::-1]:
            return count
        else:
            continue

# Q4b
def is_lychrel_suspect(n, t):
    pal = n
    for i in range(t):
        string_pal = str(pal)[::-1]
        pal += int(string_pal)
        if str(pal) == str(pal)[::-1]:
            return False
    return True
# Q4c
def lychrel_sort(numbers, t):
    non_t_lychrel = []
    t_lychrel = []
    for i in range(len(numbers)):
        if is_lychrel_suspect(numbers[i], t):
            non_t_lychrel.append((numbers[i], i))
        else:
            t_lychrel.append((numbers[i], lychrel_loops(numbers[i]), i))
    t_lychrel2 = sorted(t_lychrel, key=lambda num: num[1])
    non_t_lychrel2 = sorted(non_t_lychrel, key=lambda num: num[1])
    final_list = [num[0] for num in t_lychrel2]
    for i in range(len(non_t_lychrel2)):
        final_list.append(non_t_lychrel2[i][0])
    return final_list
##############
# QUESTION 5 #
##############
# Q5a
def calculate_grades_v1(grades):
    final_grades = []
    for grade in grades:
        if grade[0] >= sum(grade[1])/3:
            final_grades.append(grade[0])
        else:
            final_grade = sum(grade[1])/3*0.1 + grade[0]*0.9
            final_grades.append(final_grade)
    return final_grades
# Q5b
def calculate_grades_v2(grades, w, f):
    final_grades = []
    for grade in grades:
        final_grade = w*(f(grade[0])) + (1-w)*(sum(grade[1])/3)
        final_grades.append(final_grade)
    return final_grades
# Q5c_i
def two_largest_values_average(tup):
    return (sorted(tup)[2] + sorted(tup)[1])/2

def calculate_grades_v3(grades, w):
    final_grades = []
    for grade in grades:
        final_grades.append(w*grade[0] + (1-w)*(two_largest_values_average(grade[1])))
    return final_grades
# Q5c_ii
def calculate_w(grades, target_average):
    sum_tests = sum([grade[0] for grade in grades])
    sum_assignments = sum([two_largest_values_average(grade[1]) for grade in grades])
    w = (target_average*len(grades) - sum_assignments)/(sum_tests - sum_assignments)
    if w > 1 or w < 0:
        return None
    else:
        return w

calculate_w([(95, (85, 90, 95)), (90, (90, 92, 100))], 93.025)
##########
# Tester #
##########

def test():
    if divisors(6) != [1, 2, 3] or divisors(7) != [1]:
        print("Error in Q1a")

    if perfect_numbers(2) != [6, 28]:
        print("Error in Q1b")

    if abundant_density(20) != 0.15:
        print("Error in Q1c")

    if not semi_perfect_4(20) or semi_perfect_4(28):
        print("Error in Q1e")

    for i in range(10):
        if coin() not in {True, False}:
            print("Error in Q2a")
            break

    for i in range(10):
        if roll_dice(6) not in {1, 2, 3, 4, 5, 6}:
            print("Error in Q2b")
            break

    for i in range(10):
        if (roulette(100, "even") not in {0, 200}) or (roulette(100, "odd") not in {0, 200}):
            print("Error in Q2c")
            break

    shuffled_list = shuffle_list([1, 2, 3, 4])
    for i in range(1, 5):
        if i not in shuffled_list:
            print("Error in Q2e")
            break

    if inc("0") != "1" or \
            inc("1") != "10" or \
            inc("101") != "110" or \
            inc("111") != "1000" or \
            inc(inc("111")) != "1001":
        print("Error in Q3a")

    if add("0", "1") != "1" or \
            add("1", "1") != "10" or \
            add("110", "11") != "1001" or \
            add("111", "111") != "1110":
        print("Error in Q3b")

    if pow_two("10", 2) != "1000" or \
            pow_two("111", 3) != "111000" or \
            pow_two("101", 1) != "1010":
        print("Error in Q3c")

    if div_two("10", 1) != "1" or \
            div_two("101", 1) != "10" or \
            div_two("1010", 2) != "10" or \
            div_two("101010", 3) != "101":
        print("Error in Q3d")

    if not leq("1010", "1010") or \
            leq("1010", "0") or \
            leq("1011", "1010"):
        print("Error in Q3e")

    if lychrel_loops(28) != 2 or lychrel_loops(110) != 1:
        print("Error in Q4a")

    if (not is_lychrel_suspect(28, 1)) or is_lychrel_suspect(28, 2) or is_lychrel_suspect(28, 3):
        print("Error in Q4b")

    if lychrel_sort([165, 164, 28, 110, 196], 8) != [110, 28, 165, 164, 196]:
        print("Error in Q4c")

    grades = [(95, (85, 90, 95)), (90, (90, 92, 100))]
    if calculate_grades_v1(grades) != [95, 90.4]:
        print("Error in Q5a")

    grades = [(95, (85, 90, 95)), (90, (90, 92, 100))]
    w = 0.7
    f = lambda x: min(100, x + 3)
    if calculate_grades_v2(grades, w, f) != [95.6, 93.3]:
        print("Error in Q5b")

    grades = [(95, (85, 90, 95)), (90, (90, 92, 100))]
    w = 0.7
    if calculate_grades_v3(grades, w) != [94.25, 91.8]:
        print("Error in Q5c_i")

    grades = [(95, (85, 90, 95)), (90, (90, 92, 100))]
    target_average = 93.025  # This is the average of [94.25, 91.8]
    if abs(calculate_w(grades, target_average) - 0.7) > 0.000001:
        print("Error in Q5c_ii")




