

def recursion_countdown(num):

    if num <= 0:
        return "Recursion Closed"
    print(num)
    recursion_countdown(num-1)

# print(recursion_countdown(3))


def summing_numbers(num):

    if num == 1:
        print("Print sum reached its limit 1")
        return 1

    print(f"Number before getting recursion {num} calls to {num - 1}")
    result =  num + summing_numbers(num - 1)
    print(f"Sum of result {result}")
    return result

# print(summing_numbers(5))



###########  reverse the string using recursion #################


def reverse_string(str):

    if len(str) == 0:             # create a base conditon where length of a string should be 0
        return str                # Once string reaches it's limit return the string
    return reverse_string(str[1:]) + str[0]    # if not then function call itself from the substring beginning with second characters

# print(reverse_string("hello"))


################ Fibonacci Series using recursion #################

def fibonacci_series(num):
    if num < 2:
        return 1
    return fibonacci_series(num - 1) + fibonacci_series(num - 2)

# print(fibonacci_series(8))


############## Factorial Using recursion ###################


def factorial(num):
    if num == 0 or num == 1:   # base condtion is if value is 0 or 1 then return 1
        return 1
    return num * factorial(num - 1) # self call the funcation and multiply values by subtracting the value in recursion

# print(factorial(1000))



############## Power base recursion ##################


def power(base, expo):
    if expo == 0:
        return 1
    else:
        return base * power(base,expo-1)

# print(power(5,2))




############   Sum of Array ########


def sumOf_array(arr):

    if len(arr) == 0:
        return 0
    else:
        return arr[0] + sumOf_array(arr[1:])

# print(sumOf_array([1,2,4,5,6]))


############  Number range  ######


def numRange(start, end):
    if start == end:
        return [end]
    result = numRange(start, end - 1)
    result.append(end)
    return result

# print(numRange(1,6))


#################  Flattern Array ###############


def flattern_array(arr):

    arr1 = []

    for i in arr:
        if type(i) == list:
            arr1 = arr1 + flattern_array(i)
        else:
            arr1.append(i)
    return arr1

# print(flattern_array([1,2,[3,4,[5,6],7,[8]],9,10]))

################   Permutation Combination  ###############


def permutation_combination(ste):
    result = []

    if len(ste) == 0:
        result.append("")
        return result
    for i in range(len(ste)):
        first_char = ste[i]
        rest_str = ste[:i] + ste[i+1:]
        sub_permutation = permutation_combination(rest_str)

        for j in sub_permutation:
            result.append(first_char+j)
    return result

# print(permutation_combination("dog"))


########### Sum of N natual numbers ###########

def sum(n):
    if n == 0:
        return 0
    return n + sum(n-1)

# print(sum(4))

###### Palindrome ############


def palindome(ste):
    if len(ste) <= 1:
        return True
    if ste[0] != ste[-1]:
        return False
    return palindome(ste[1:-1])

# print(palindome("Dheeraj"))


##### Count of Digit   ######

def digit(num):
    if num == 0:
        return 0
    return 1 + digit(num // 10)

print(digit(7))


##### Sum Of digit ######


def sumDdigit(num):
    if num == 0:
        return 0
    return (num % 2) + digit(num // 10)

print(sumDdigit(10))


def sort_array(arr):
    if len(arr) <= 0:
        return True
    if arr[0] > arr[1]:
        return False
    return sort_array(arr[1:])

# print(sort_array([1,5,3,2,7,0]))

def count_vowel(s):
    if not s:
        return 0
    first = 1 if s in 'aeiou' else 0
    return first + count_vowel(s[1:])

print(count_vowel("rtedfsdfsdfs"))


def reprt_str(ste,n):
    if  n == 0:
        return ""
    return ste + reprt_str(ste , n - 1)
print(reprt_str("Dheeraj",2))


def min_arr(arr):
    if len(arr) == 1:
        return arr[0]
    return min(arr[0], min_arr(arr[1:]))

print(min_arr([3,4,6,7,8,6,42]))


def count_occurance(s, char):
    if not s:
        return 0
    return (1 if s[0] == char else 0) + count_occurance(s[1:],char)

# count_occurance(4,"Dheeraj")


def newPermute(ste):
    result = []

    if len(ste) == 0:
        result.append("")
        return result
    for i in range(len(ste)):
        fn = ste[i]
        rest_str = ste[:i] + ste[i+1:]
        subpremute = newPermute(rest_str)

        for j in subpremute:
            result.append(fn + j)

    return result

# print(newPermute("constantinopal"))


def print_digit_lf_rg(num):
    if num < 10:
        print(num)
        return num
    print(num // 10)
    print_digit_lf_rg(num % 10)
# print_digit_lf_rg(11)

def replace_all_char_x_with_y(s):
    if not s:
        return ""
    char = "y" if s[0] == "x" else s[0]
    return char + replace_all_char_x_with_y(char[1:])

# print(replace_all_char_x_with_y("xxyyxx"))


def adjecent_number(n):
    s = str(n)
    if len(s) <= 1:
        return s
    return s[0] + "-" + adjecent_number(int(s[1:]))

# print(adjecent_number("132423432234"))


def count_of_(n):
    if n == 0:
        return 0
    return count_of_(n-1)

# print(count_of_(110))


def multiply(a,b):
    if b == 0:
        return 0
    return a + multiply(a,b-1)

print(multiply(2,8))


def even_arr(arr):
    if not arr:
        return True
    if arr[0] % 2 != 0:
        return False
    return even_arr(arr[1:])

# print(even_arr([2,4,5,6,7,8]))



# write a code using sliding window where k = 3 and find sum of greater number

def shifting_window(arr, k = 3):
    max_sum = 0
    current_sum = 0

    for i in range(0,len(arr)-k-1):
        print(arr[i])
        max_sum += arr[i]

    for j in range(arr[i], arr[i+k]):
        print(arr[i])



shifting_window([1,5,7,14,3,9,1])