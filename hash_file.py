def get_val():
    pass

empy_onj = object()


t = {1:"john",2:"JOE",3:"JACOB",get_val():"empty function",empy_onj:"remp"}
t[get_val()] = "Jenny"
t[1] = "get"


# print(t.values())

import re
from collections import defaultdict

def word_frequency(ste):
    get_word_list = re.split("\W+",ste.lower())
    get_default_dict = defaultdict(int)

    for word in get_word_list:
        if word:
            get_default_dict[word] += 1

    return get_default_dict

# print(word_frequency("get outside of my house my"))



def create_phonebook(list_value):
    new_dict = {}

    for i in list_value:
        get_new_val = i.split(":")
        new_dict[get_new_val[0]] = get_new_val[1]

    return new_dict

# print(create_phonebook(["John:124345","Jack:67876564","Jenny:1577543"]))


# ["doctor","act","Tac","listen",'silent','enlist','world']



def create_anagram(l1):
    anagram_dict = defaultdict(list)

    for i in l1:
        sorted_val = "".join(sorted(i.lower()))
        anagram_dict[sorted_val].append(i)

    return list(anagram_dict.values())

# print(create_anagram(["doctor","act","Tac","listen",'silent','enlist','world']))


def create_a_set(l1, l2):
    a = set(l1)
    b = set(l2)
    print(a-b)
    print(b-a)
    print(sorted(list(a-b)+list(b-a)))
    result = list((a-b).union(b-a))
    return result

# print(create_a_set([1,2,3,5],[1,3,4,6,8,9]))

def two_sum(nums:list[int],target:int):
    num_map = {}

    for i, num in enumerate(nums):
        complement = target - num

        if complement in num_map:
            return [num_map[complement],i]
        num_map[num] = i
    return num_map

# print(two_sum([2,7,11,15],9))



def longest_consecutive_sequence(nums):
    nums_sets = set(nums)
    longest = 0

    for i in nums_sets:
        if i - 1 not in nums_sets:
            current = i
            count = 1

            while current + 1 in nums_sets:
                current += 1
                count += 1

            longest = max(longest, count)

    return longest

# print(longest_consecutive_sequence([100,1,200,3,4,5,6]))


class hashtable():

    def __init__(self, limit = 14):
        self.limit = limit
        self.storage = [None] * self.limit

    def _hash(self, key, max_val):
        hash_val = 0
        for i in key:
            hash_val += ord(i)
        return hash_val % max_val


    def set(self,key, value):
        index = self._hash(key,self.limit)
        if self.storage[index] is None:
            self.storage[index] = [[key,value]]
        else:
            for pair in self.storage[index]:
                if pair[0] == key:
                    pair[1] = value
                    return
            self.storage[index].append([key,value])

    def get(self,key):
        index = self._hash(key,self.limit)
        if self.storage[index]:
            for pair in self.storage[index]:
                if pair[0] == key:
                    return pair[1]

        return None

    def remove(self,key):
        index = self._hash(key,self.limit)
        if self.storage[index]:
            if len(self.storage[index]) == 1 and self.storage[index][0][0] == key:
                self.storage[index] = None
            else:
                for i, pair in enumerate(self.storage[index]):
                    if pair[0] == key:
                        del self.storage[index][i]
                        break

    def has(self,key):
        index = self._hash(key,self.limit)
        if self.storage[index]:
            for pair in self.storage[index]:
                if pair[0] == key:
                    return True
        return False


    def print_all(self):
        for i in range(self.limit):
            if self.storage[i] is not None:
                print(f"Bucket {i} :- {self.storage[i]}")
            else:
                print(f"Bucket {i} is empty")


hash = hashtable()
hash.set("jack","998822993")
hash.set("jill","874930210")
print(hash.get("Jacob"))
# print(hash.remove("jill"))
print(hash.print_all())


def word_frequecy(text:str,word:str):
    words = re.split("\W+",text.lower())
    target = word.lower()
    hash_table = hashtable()

    for current in words:
        if current == "":
            continue

        if hash_table.has(current):
            hash_table.set(current,hash_table.get(current) + 1)
        else:
            hash_table.set(current, 1)

    return hash_table.get(target) or 0

print(word_frequecy("where are you my friend", "you"))


