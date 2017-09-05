def odd_even():
    for num in range(1, 2001):
        if num % 2 == 0:
            num_as_str = str(num)
            print "Number is " + num_as_str + ". This is an even number."
        else:
            num_as_str = str(num)
            print "Number is " + num_as_str + ". This is an odd number." 

# odd_even()

a = [2,4,6]
def multiply(target_list, num):
    output = []
    for val in target_list:
        multi = val * num
        output.append(multi)
    return output

# b = multiply(a,5)
# print b

def layered_multiples(arr):
    output = []
    for num in arr:
        temp_list = []
        for i in range(num):
            temp_list.append(1)
        output.append(temp_list)
    return output

c = layered_multiples(multiply(a,3))
print c