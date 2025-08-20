import string

from Code_stack import stack


def reversing_string(valStr):
    s = stack()
    t = ""
    for i in valStr:
        s.push(i)

    while s.stack:
        t += "".join(s.pop())

    if valStr == t:
        return True
    else:
        return False

print(reversing_string("abcdcbaa"))


def palindome(valStr):
    val_str1 = valStr[::-1]
    if val_str1 == valStr:
        return True
    else:
        return False


print(palindome("abcdcba"))




def create_valid_id(ip):

    list_of_ip = []

    for i in range(1, min(len(ip),4)):
        ip_creation = ["","","",""]

        ip_creation[0] = ip[:i]

        if not valid_ip(ip_creation[0]):
            continue

        for j in range(i + 1, i + min(len(ip) - i,4)):
            ip_creation[1] = ip[i:j]

            if not valid_ip(ip_creation[1]):
                continue

            for k in range(j + 1, j + min(len(ip) - j, 4)):
                ip_creation[2] = ip[j:k]
                ip_creation[3] = ip[k]

                if valid_ip(ip_creation[2]) and valid_ip(ip_creation[3]):
                    list_of_ip.append(".".join(ip_creation))

    return list_of_ip



def valid_ip(string):

    conv_str_int = int(string)

    if conv_str_int > 255:
        return False

    return len(string) == len(str(conv_str_int))

# print(create_valid_id("1921680"))


### find the largest Palindrome ####

def largest_palindrome(string):

    for i in range(len(string)):
        string1 = string[i :len(string) - 1]
        check_palindrome(string1)

def check_palindrome(string):
    if string == string[::-1]:
        return True



# print(largest_palindrome("abaxyzzyxf"))



def find_common_value_in_list(l1):
    t = dict()
    get_str = list(set("".join(l1)))
    counter = 0
    for i in get_str:
        for j in l1:
            if i not in j:
                t.pop(i,None)
                break
            else:
                counter += 1
            t[i] = counter

    print(t)

# find_common_value_in_list(["abc", "bcd", "cbaccd"])



def non_repeting_char(string):

    for i in set(string):
        if string.count(i) == 1:
            print(i)

# reversing_string("abcdcaf")


non_repeting_char("abcdcaf")

def reverse_word_in_string(string):

    new_val = " ".join(string.split(" ")[::-1])
    print(new_val)

reverse_word_in_string("RSTForum is the best!")




def generate_string(document,characters):

    print(sorted(document))
    print(sorted(characters))


    for val in document:
        get_document_count = get_frequency_count(val,document)

        get_character_count = get_frequency_count(val,characters)

        if get_document_count > get_character_count:
            return False

    return True


def get_frequency_count(document, taget):
    frequency = 0
    for tar in taget:
        if tar == document:
            frequency += 1
    return frequency

print(generate_string("uRo!t FsiheBST rm ", "RSTForum is the Best!"))



def semordnilp(words):
    new_match = []
    matching_list = words
    for i in words:
        reverse_word = i[::-1]
        if reverse_word in matching_list and reverse_word != i:
            new_match.append([i, reverse_word])
            matching_list.remove(i)
            matching_list.remove(reverse_word)
    return new_match


print(semordnilp(["diaper", "abc", "test", "cba", "repaid"]))
















