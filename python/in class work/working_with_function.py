
def print_hello_world():
    print("Hello Word!!!!")
    print("How are you?")

print_hello_world()
print_hello_world()
print_hello_world()

def print_persons_name(first_name, last_name):
    print(first_name + last_name)

print_persons_name('Claire', 'Feng')

def min(list_of_numbers):

    list_of_numbers.sort()
    return list_of_numbers[0]
    #print(list_of_numbers[0])

numbers = [10,2,-100,40,37]

smallest_number = min(numbers)

print("Smallest Number: " + str(smallest_number))
#min(numbers)

