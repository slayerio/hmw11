# a
number: tuple[int] = (99,)
# b
numbers1: tuple[int, ...] = (77, 88, 99)
print(numbers1)


# c
def len_tup(a: tuple[str, ...]):
    print(len(a))


len_tup(('only', 'for', 'the', 'len'))


# d
def two_tup(a, b: tuple) -> tuple:
    return a[0] + ', ' + b[0]


info_1 = ('name: danny',)
info_2 = ('age: 22',)
print(two_tup(info_1, info_2))


# e
def common(a, b: tuple) -> tuple:
    return tuple(i for i in a if i in b)


nums1 = (3, 2, 6)
nums2 = (1, 2, 3)
print(common(nums1, nums2))


# f
def not_common(a, b: tuple) -> tuple:
    tuple_1 = tuple(i for i in a if i not in b)
    tuple_2 = tuple(i for i in b if i not in a)
    return tuple_1 + tuple_2


nums3 = (3, 2, 6, 7)
nums4 = (1, 2, 3, 5)
print(not_common(nums3, nums4))


# g
def tuple_index(a: tuple, b: int):
    if b < 0 or b >= len(a):
        return None
    else:
        return a[b]


tup_1 = (10, 20, 30, 40, 50)
print(tuple_index(tup_1, 4))
print(tuple_index(tup_1, 7))


# h
def reverse_tup(a: tuple) -> tuple:
    return a[::-1]


tup_2 = (1, 2, 3, 4)
print(reverse_tup(tup_2))


# i
def tup_num_without_remainder(a: tuple, b: int) -> int:
    tuple_remainder = [i for i in a if not b % i]
    return len(tuple_remainder)


x = tup_num_without_remainder((10,9,5,2), 7)
print(x)


# j
def tup_num_multi(a: tuple, b: int) -> tuple:
    return a * b


multiplication = tup_num_multi((1, 2), 3)
print(multiplication)


# k
def index_value(a: tuple) -> tuple:
    """
    enumerate - counts the index of which the value is
    with this, created new tuple containing index and value
    """
    return tuple((index, value) for index, value in enumerate(a))


tup_3 = index_value(('Apple', 'Banana', 'Orange'))
print(tup_3)


# l
def tup_dict(a: tuple[int, ...]) -> dict:
    return {
        'max number': max(a),
        'min number': min(a),
        'tuple len': len(a),
        'tuple avg': sum(a) / len(a),
        'sorted tuple': sorted(a),
        'reverse sorted tuple': sorted(a, reverse=True)
    }


tuple_for_dict = tup_dict((3, 5, 7, 9))
print(tuple_for_dict)


# m
def letter_tup(a: tuple) -> str:
    return ''.join(a)


tup_let = letter_tup(('H', 'e', 'l', 'l', 'o'))
print(tup_let)


# n
def str_letter(a: str) -> tuple:
    return tuple(a)


str_let = str_letter('hello')
print(str_let)


# o
def remove_num(a: tuple, b: int) -> tuple:
    return tuple(i for i in a if i != b)


print(remove_num((10, 20, 30, 35, 10, 47), 10))


# p
def no_double(a: tuple) -> tuple:
    tup_list = []
    for i in range(len(a)):
        tup_list.append(a[i]) if a[i] not in tup_list else ''
    return tuple(tup_list)


double = no_double((10, 20, 10, 40))
print(double)


# q
def num_append(a: tuple, b: int) -> tuple:
    result = []
    for i in range(len(a)):
        result.append(i) if a[i] == b else ''
    return tuple(result)


test = num_append((2, 3, 5, 5, 8, 7), 5)
print(test)


# r
x = ''
grades = []
y = ''
names: list[str] = []

while True:
    try:
        x = int(input("whats your grade"))
        if 0 <= x <= 100:
            grades.append(x)
        elif x == -999:
            break
        else:
            print("please enter a number between 0-100")
            continue
    except ValueError:
        print("enter a number, not str")


while True:
    y = input("whats your name")
    if y == 'done':
        break
    try:
        int(y)
        print("enter a valid name")
    except ValueError:
        names.append(y)


names_tup = tuple(names)
grades_tup = tuple(grades)
names_grades_tup = tuple(zip(names, grades))
print(names_grades_tup)