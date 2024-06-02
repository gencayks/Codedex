def apply_operation(operation, numbers):
    result = []
    for num in numbers:
        result.append(operation(num))
    return result

#example operation

def double(x):
    return 2*x


#list of numbers
numbers_list = [1, 2, 3, 4, 5]

doubled_numbers = apply_operation(double, numbers_list)

print("original numbers list: ", numbers_list)
print("doubled numbers list: ", doubled_numbers)
