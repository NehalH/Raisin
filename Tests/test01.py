import random

def generate_random_numbers(n):
    random_numbers = [random.random() for _ in range(n)]
    random_numbers.sort(reverse=True)
    return random_numbers

def multiply_lists(list1, list2):
    result = 0
    for i in range(len(list1)):
        result += list1[i] * list2[i]
    return result

def is_squishy_right(list1, list2, list3):
    if multiply_lists(list1, list2) < multiply_lists(list1, list3):
        return True
    else:
        return False

iterations = 100
frq_list_size = 10
list2 = [1,1,2,2,2,2,3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,5,5,5,5,5,5,5,5,5]
list3 = [2,2,2,4,4,4,4,4,4,4,4,4,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6]
squishy = 0
cheesecake = 0

while iterations!=0:
    iterations -= 1
    list1 = generate_random_numbers(frq_list_size)
    if is_squishy_right(list1, list2, list3)==True:
        squishy += 1
    else:
        cheesecake += 1

if squishy>cheesecake:
    print('Squishy is Right')
    print(f'Squishy: {squishy} \nCheesecake: {cheesecake}')
elif squishy<cheesecake:
    print('Cheesecake is right')
    print(f'Squishy: {squishy} \nCheesecake: {cheesecake}')